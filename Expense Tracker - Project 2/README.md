
# Expense Tracker – CLI

A simple, human-friendly **command-line Expense Tracker** that helps you log daily spending, review today’s expenses, and see how much you’ve spent over a custom time interval.

This is Project 2 of a personal “6‑month, 50 projects” learning challenge.

***

## Features

- **Add expenses quickly**
  - Save date, amount, category, and a short description
- **View today’s spending**
  - See the **total spent today** and a breakdown of each expense
- **View expenses over a custom date range**
  - Choose any start and end date (up to 50 days apart)
  - See total spending and all expenses in that interval
- **Delete incorrect entries**
  - Remove expenses that were added by mistake
- **Simple menu-driven CLI**
  - Type short commands like `add`, `today`, `interval`, `delete`, `exit`

All data is stored locally in a JSON file (`expenses.json`).

***

## Project Structure

```text
Expense Tracker - Project 2/
├── main.py                 # Entry point for the application
├── menu.json               # Command names and their descriptions
├── expenses.json           # Stored expenses (created automatically if missing)
├── .gitignore              # Ignore cache/temporary files
├── LICENSE                 # Project license
├── README.md               # This file
└── src/
    ├── __init__.py
    ├── add_expenses.py     # Add a new expense
    ├── delete_expense.py   # Delete an existing expense
    ├── daily_expense.py    # Show today’s total and detailed expenses
    ├── custom_time_expense.py # Show total + details over a custom interval
    └── user_input.py       # Map user commands to the correct functions
```

***

## Requirements

- **Python 3.8+**
- No external libraries required (only uses the standard library: `json`, `datetime`)

***

## Installation & Setup

1. Clone or download the repository.
2. Open a terminal in the project folder:

   ```bash
   cd "Expense Tracker - Project 2"
   ```

3. Make sure `menu.json` looks similar to:

   ```json
   {
     "menu": {
       "add": "Add a new expense",
       "delete": "Delete an expense",
       "today": "View today's expenses",
       "interval": "View expenses over an interval",
       "exit": "Exit the application"
     }
   }
   ```

4. If `expenses.json` does not exist, it will be created automatically when you add your first expense.

***

## Usage

Run the application from the project root:

```bash
python main.py
```

You’ll see a menu like:

```text
Welcome to the Expense Management Application!

Available Commands:
- add: Add a new expense
- delete: Delete an expense
- today: View today's expenses
- interval: View expenses over an interval
- exit: Exit the application
```

Type a command and press Enter.

***

### 1. Add an Expense

Command: `add`

You will be asked for:

- **Date** (`YYYY-MM-DD`) – leave blank for **today**
- **Amount** – numeric, must be positive
- **Category** – e.g. Food, Transport, Rent
- **Description** – short note like “pizza treat with sister”

Example:

```text
Enter the date of the expense (YYYY-MM-DD) or leave blank for today:
Enter the amount of the expense: 1200
Enter the category of the expense (e.g., Food, Transport, Utilities): Food
Enter a brief description of the expense: Spent on pizza treat to sister
Expense added successfully.
```

***

### 2. View Today’s Expenses

Command: `today`

Shows:

- Total spent today
- Each individual expense

Example:

```text
Total expenses for today (2025-11-27): $1200.00
Here are the expenses for today:
- Food: $1200.00 (Spent on pizza treat to sister)
```

***

### 3. View Expenses Over an Interval

Command: `interval`

- Enter a **start date** and **end date** (`YYYY-MM-DD`).
- The interval is capped at **50 days** to keep things simple and fast.

Example:

```text
Enter the start date (YYYY-MM-DD): 2025-11-01
Enter the end date (YYYY-MM-DD): 2025-11-15

Total expenses from 2025-11-01 to 2025-11-15: $4850.00
Here are the expenses for this timeframe:
- 2025-11-02 | Food: $750.00 (Lunch with friends)
- 2025-11-05 | Transport: $150.00 (Bus pass)
...
```

If there are no expenses in that range, the app tells you so.

***

### 4. Delete an Expense

Command: `delete`

This module lets you remove incorrect or unwanted entries from `expenses.json`.  
(The exact interaction depends on how deletion is implemented: by index, date+category, etc.)

***

### 5. Exit the Application

Command: `exit`

Cleanly exits the CLI:

```text
Exiting the application. Goodbye!
```

***

## Data Format

Expenses are stored in `expenses.json` as a list of objects:

```json
[
  {
    "date": "2025-11-27",
    "amount": 1200.0,
    "category": "Food",
    "description": "Spent on pizza treat to sister"
  }
]
```

This simple structure makes it easy to:

- Filter by date or interval
- Summarize totals
- Extend the app later (e.g., per-category summaries, exports)

***

## Possible Future Improvements

- Per-category summaries (e.g., total Food/Transport/etc.)
- Monthly/weekly reports
- Export to CSV
- Better delete/edit UI (select by ID/index)
- Basic charts using external tools

***

## Author

**Ujjwal Babu Bhatta**  
