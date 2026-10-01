# Student Grade Manager

A simple Python command-line application that stores student marks, calculates grades, and displays class statistics.

## Features

* Add multiple students
* Store student name, mark, and grade
* Calculate grades automatically
* Allow duplicate student names
* Display results in a neatly aligned table
* Calculate:

  * Class average
  * Highest mark
  * Lowest mark
* Menu-driven interface
* Handles invalid input without crashing

## Grade System

| Mark     | Grade |
| -------- | ----- |
| 90 - 100 | A     |
| 80 - 89  | B     |
| 70 - 79  | C     |
| 60 - 69  | D     |
| Below 60 | E     |

Marks must be between **0 and 100**.

Invalid inputs such as:

* `105`
* `-5`
* `abc`

are rejected and the user is asked to enter the mark again.

## Data Structure

The program uses a **list of dictionaries** to store students.

Example:

```python
students = [
    {
        "name": "Priya",
        "mark": 85,
        "grade": "B"
    },
    {
        "name": "Priya",
        "mark": 72,
        "grade": "C"
    }
]
```

A list was intentionally chosen because it allows multiple students to have the same name.

## Project Structure

```text
Day2/
├── grade_manager.py
├── README.md
├── .gitignore
└── .venv/
```

The `.venv` directory is excluded from Git using `.gitignore`.

## Requirements

* Python 3.12 or later
* No external Python packages are required.

## How to Run

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Open the project

```bash
cd Day2
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Run the program

```bash
python grade_manager.py
```

## Example

```text
Student Grade Manager
1. Add student
2. Show results
3. Quit

Enter your choice: 1

Enter student name: Priya
Enter mark (0-100): 85

Student 'Priya' added successfully.

Student Grade Manager
1. Add student
2. Show results
3. Quit

Enter your choice: 2

========================================
Name                Mark      Grade
----------------------------------------
Priya               85.00     B
----------------------------------------
Class Average : 85.00
Highest Mark  : 85.00
Lowest Mark   : 85.00
========================================
```

## Learning Goals

This project practices:

* Variables
* Lists
* Dictionaries
* Functions
* `if / elif / else`
* `while` loops
* `try / except`
* User input validation
* String formatting
* Basic statistics
* Python virtual environments
* Git and GitHub
