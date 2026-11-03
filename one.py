"""Analyze student ratings and comments from a CSV file."""

import re
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


STOP_WORDS = {"and", "but", "the", "is", "a", "of", "too"}
REQUIRED_COLUMNS = {"StudentID", "Rating", "Comment"}


def load_feedback(file_path):
    """Read a CSV file and validate its ratings."""
    try:
        feedback = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: File not found: {file_path}")
        return None
    except pd.errors.EmptyDataError:
        print(f"Error: The file is empty: {file_path}")
        return None
    except pd.errors.ParserError as error:
        print(f"Error: Could not read the CSV file: {error}")
        return None

    return validate_feedback(feedback)


def validate_feedback(feedback):
    """Keep rows with whole-number ratings from 1 to 5."""
    missing_columns = REQUIRED_COLUMNS - set(feedback.columns)
    if missing_columns:
        missing_list = ", ".join(sorted(missing_columns))
        print(f"Error: CSV is missing required column(s): {missing_list}")
        return None

    valid_rows = []
    for row_number, row in enumerate(feedback.itertuples(index=False), start=1):
        try:
            rating_number = float(row.Rating)
        except (TypeError, ValueError):
            rating_number = 0.0

        if not rating_number.is_integer() or not 1 <= rating_number <= 5:
            print(
                f"Warning: Row {row_number} skipped - rating must be a whole "
                "number from 1 to 5."
            )
            continue

        valid_rows.append(
            {
                "StudentID": row.StudentID,
                "Rating": int(rating_number),
                "Comment": "" if pd.isna(row.Comment) else str(row.Comment),
            }
        )

    return pd.DataFrame(valid_rows, columns=["StudentID", "Rating", "Comment"])


def enter_feedback():
    """Collect feedback rows from the keyboard without needing a CSV path."""
    rows = []
    while True:
        print(f"\nEnter feedback row {len(rows) + 1}")
        student_id = input("Student ID: ").strip()
        rating = input("Rating (1-5): ").strip()
        comment = input("Comment: ").strip()
        rows.append({"StudentID": student_id, "Rating": rating, "Comment": comment})

        add_another = input("Add another row? (y/n): ").strip().lower()
        if add_another != "y":
            break

    feedback = pd.DataFrame(rows, columns=["StudentID", "Rating", "Comment"])
    return validate_feedback(feedback)


def choose_feedback():
    """Let the user choose a test dataset or enter feedback manually."""
    project_folder = Path(__file__).parent
    while True:
        print("\nChoose the input data")
        print("1. Test Case 1: Normal sample (6 rows)")
        print("2. Test Case 2: One-row minimum input")
        print("3. Test Case 3: Invalid ratings")
        print("4. Enter feedback rows manually")
        print("5. Exit")
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            feedback = load_feedback(project_folder / "feedback.csv")
        elif choice == "2":
            feedback = load_feedback(project_folder / "test_data" / "minimum_input.csv")
        elif choice == "3":
            feedback = load_feedback(project_folder / "test_data" / "invalid_ratings.csv")
        elif choice == "4":
            feedback = enter_feedback()
        elif choice == "5":
            return None
        else:
            print("Please enter 1, 2, 3, 4, or 5.")
            continue

        if feedback is not None:
            return feedback


def show_summary(feedback):
    """Print the number of valid ratings, average, counts, and common words."""
    print(f"\nValid feedback: {len(feedback)}")

    if feedback.empty:
        print("Average rating: N/A (no valid feedback)")
    else:
        print(f"Average rating: {feedback['Rating'].mean():.2f}")

    print("Ratings: " + ", ".join(
        f"{rating} -> {(feedback['Rating'] == rating).sum()}"
        for rating in range(5, 0, -1)
    ))

    word_counts = {}
    for comment in feedback["Comment"]:
        words = re.findall(r"[a-zA-Z]+", comment.lower())
        for word in words:
            if word not in STOP_WORDS:
                word_counts[word] = word_counts.get(word, 0) + 1

    top_words = sorted(word_counts.items(), key=lambda item: (-item[1], item[0]))[:3]
    if top_words:
        word_list = ", ".join(f"{word} ({count})" for word, count in top_words)
        print(f"Top 3 words: {word_list}")
    else:
        print("Top 3 words: no words found")


def show_sentiment(feedback):
    """Print sentiment totals and display a bar chart."""
    positive = int(feedback["Rating"].isin([4, 5]).sum())
    neutral = int((feedback["Rating"] == 3).sum())
    negative = int(feedback["Rating"].isin([1, 2]).sum())
    total = len(feedback)

    groups = [("Positive", positive), ("Neutral", neutral), ("Negative", negative)]
    for name, count in groups:
        percentage = count / total * 100 if total else 0
        print(f"{name}: {count} ({percentage:.2f}%)")

    if total == 0:
        print("No valid feedback to display in a chart.")
        return

    names = [name for name, _ in groups]
    counts = [count for _, count in groups]
    plt.bar(names, counts, color=["seagreen", "gold", "tomato"])
    plt.title("Student Feedback Sentiment")
    plt.xlabel("Sentiment")
    plt.ylabel("Number of ratings")
    plt.tight_layout()
    plt.show()


def main():
    """Run the feedback analyzer through its interactive menus."""
    feedback = choose_feedback()
    if feedback is None:
        return

    while True:
        print("\nStudent Feedback Analyzer")
        print("1. Summary and top 3 words")
        print("2. Sentiment and bar chart")
        print("3. Choose different input data")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            show_summary(feedback)
        elif choice == "2":
            show_sentiment(feedback)
        elif choice == "3":
            new_feedback = choose_feedback()
            if new_feedback is None:
                print("Goodbye!")
                break
            feedback = new_feedback
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
