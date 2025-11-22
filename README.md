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
- #
= *Language:* Python 3.x
- *Input/Output:* Standard Console I/O
- *Data Structure:* List of Dictionaries

## 📌How to Run
```
python personal_habit_tracker.py
```
Markdown

# Personal Habit Tracker

## 1. Project Overview
The **Personal Habit Tracker** is a Python-based Command Line Interface (CLI) application designed to help users build and maintain positive routines. 

This project addresses the challenge of consistency by providing a simple, distraction-free tool to log habits, define their frequency, and track completion counts. [cite_start]It is designed with a clear logical workflow allowing users to interact seamlessly with the system[cite: 22].

## 2. Features
[cite_start]The system is built around three major functional modules[cite: 20]:

### **Module A: Habit Creation (Input)**
* **Add Habit:** Users can define custom habit names.
* **Frequency Setting:** Allows users to specify if a habit is "daily" or "weekly" to set expectations.

### **Module B: Progress Tracking (Processing)**
* **Completion Counter:** Increments a "done" counter every time a user marks a habit as complete.
* [cite_start]**Error Handling:** Includes validation to ensure users select valid habit IDs, preventing crashes[cite: 38].

### **Module C: Visualization (Output)**
* **View All:** Displays a formatted list of all active habits, their required frequency, and current progress.
* **Status Updates:** Provides real-time feedback (e.g., "Habit added!", "Marked as done!").

## 3. Technologies Used
* **Language:** Python 3.x
* **Input/Output:** Standard Console I/O
* **Data Structure:** List of Dictionaries (JSON-like structure)

## 4. Setup & Installation
[cite_start]Follow these steps to run the project locally[cite: 88]:

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/yourusername/personal-habit-tracker.git](https://github.com/yourusername/personal-habit-tracker.git)
    ```
2.  **Navigate to the Directory:**
    ```bash
    cd personal-habit-tracker
    ```
3.  **Run the Application:**
    ```bash
    python main.py
    ```

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
├── personal_habit_tracker.py
├── README.md
├── Report.pdf
├── /screenshots
└── /recordings

## 📌Author
(Neelavi Bhattacharjee)
(25BOE10049)
