# Personal Habit Tracker – Introduction to Programming Project

## 📌Overview
Personal Habit Tracker helps users record simple daily/weekly habits, mark them done,
and view progress. It's a console-based beginner-friendly program.

## 📌Features
- Add habit (name + frequency)
- Mark habit as done (increments done count)
- View all habits with done counts
- Simple menu-driven interface

## 📌Technology
- *Language:* Python 3.7
- *Input/Output:* Standard Console I/O
- *Data Structure:* List of Dictionaries

## 📌How to Run
```
python personal_habit_tracker.py
```
Markdown

## 📌Testing Instructions

1.  **Test Case 1: Add a Habit**
    * Select Option `1`.
    * Enter Name: `Reading`.
    * Enter Frequency: `Daily`.
    * *Expected Result:* System confirms "Habit added!".

2.  **Test Case 2: Mark as Done**
    * Select Option `2`.
    * Choose the number corresponding to `Reading`.
    * *Expected Result:* System confirms "Marked as done!".

3.  **Test Case 3: Invalid Input (Non-Functional Testing)**
    * Select Option `2`.
    * Enter a non-numeric value (e.g., "abc").
    * *Expected Result:* System catches the error and prints "Invalid input" without crashing.

## 📌Project Structure
PersonalHabitTracker/
* ├── personal_habit_tracker.py
* ├── README.md
* ├── Report.pdf
* ├── /screenshots
* └── /recordings

## 📌Author
(Neelavi Bhattacharjee)
(25BOE10049)
