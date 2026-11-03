# Student Feedback Analyzer

A beginner-friendly Python 3 program that reads student ratings and comments from CSV files using Pandas. You can choose a built-in assignment case or enter feedback directly in the program.

## Features

- Checks that the CSV has `StudentID`, `Rating`, and `Comment` columns.
- Skips ratings that are not whole numbers from 1 to 5 and prints a warning.
- Shows the valid feedback count, average rating, count of each rating, and three most common comment words.
- Groups ratings as positive (4–5), neutral (3), or negative (1–2), prints percentages, and displays a bar chart.
- Sorts equally common words alphabetically and ignores `and`, `but`, `the`, `is`, `a`, `of`, and `too`.
- Lets you enter feedback rows from the keyboard without supplying a file location.

## Run in VS Code

1. Open this folder in VS Code and open **Terminal → New Terminal**.
2. (Recommended) Create a virtual environment:

   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

3. Install the required packages:

   ```powershell
   python -m pip install -r requirements.txt
   ```

4. Start the program:

   ```powershell
   python main.py
   ```

The program asks you to choose the input data first. It then opens the analysis menu. Choose `3` there to switch input or `4` to exit.

## Run the Four Assignment Test Cases

Run `python main.py` once. For each case, enter the input choice first, then the analysis choice:

1. **Normal input:** Choose `1` for normal sample, then `1` for summary and top words.
2. **One-row input:** Choose `2` for minimum input, then `1` for summary and top words.
3. **Invalid ratings:** Choose `3` for invalid input, then `1` for summary and top words. The program warns that rows 7 and 8 were skipped.
4. **Sentiment:** Choose `1` for normal sample, then `2` for sentiment and the bar chart. Close the chart window to return to the menu.

Choose `3` from the analysis menu to select another case without restarting. Choose `4` to exit.

## Enter Your Own Feedback

Choose `4` from the input menu, then type a student ID, rating, and comment for each row. Answer `y` to add another row or `n` when finished. The program checks the ratings and analyzes the valid rows.
