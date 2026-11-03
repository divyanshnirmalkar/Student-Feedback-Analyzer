# Student Feedback Analyzer — Project Report

## Problem

Teachers need a quick way to understand student ratings and comments. This program reads a CSV file, checks each rating, and summarizes the valid feedback.

## Objectives

- Read `StudentID`, `Rating`, and `Comment` columns from a CSV file using Pandas.
- Accept only whole-number ratings from 1 to 5 and warn when a row is skipped.
- Calculate the average rating and count how many times each rating was given.
- Find the three most common comment words after removing the assigned stop words.
- Group ratings into positive, neutral, and negative sentiment and show a bar chart.
- Let the user select a built-in test case or type feedback rows into the program.

## Program Steps

1. Choose a built-in test dataset or enter feedback rows using the keyboard.
2. Read built-in CSV files with Pandas and check that all three required columns are present.
3. Read each rating and skip it with a warning if it is not a whole number from 1 to 5.
4. Show the summary and word counts, or show sentiment totals and the chart, based on the menu choice.
5. Change the input or exit from the menu.

## Testing Results

- **Normal input:** 6 valid rows, average `3.83`, rating counts `5: 2`, `4: 2`, `3: 1`, `2: 1`, `1: 0`, and top words `great (3)`, `notes (3)`, `clear (2)`.
- **One-row input:** 1 valid row, average `5.00`, and top word `great (1)`.
- **Invalid ratings:** rows 7 and 8 are skipped with warnings; the remaining 6 rows have average `3.83`.
- **Sentiment:** positive `4 (66.67%)`, neutral `1 (16.67%)`, and negative `1 (16.67%)`; the program displays the bar chart.
- **Missing file:** the program prints a clear error and stops safely.

The case-specific CSV files are selected through the program menu. See [README.md](README.md) for the exact menu choices for each case.

## Run the Project

See [README.md](README.md) for VS Code setup and run commands.
