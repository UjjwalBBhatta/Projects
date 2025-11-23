Daily Habit Tracker
A simple command-line habit tracking application that helps you build and maintain positive habits through daily tracking and streak monitoring.

Features
 Track Daily Habits - Log your daily habit completions with simple yes/no responses

 Custom Habits - Add your own habits beyond the default set

 Streak Counter - View your current streaks to stay motivated

 Flexible Management - Add or remove habits from your tracking list anytime

 Persistent Storage - All data saved locally in JSON format

Project Structure
text
Daily Habit Tracker - Project 1/
├── main.py              # Entry point for the application
├── habits.json          # Stores default, custom, and tracked habits
├── tracking.json        # Daily habit completion logs
├── menu.json            # Menu configuration
└── src/
    ├── __init__.py
    ├── custom_habits.py    # Add custom habits
    ├── streak_counter.py   # Calculate and display streaks
    ├── tracking.py         # Daily habit tracking logic
    ├── user_habits.py      # Manage tracking list
    └── user_inputs.py      # Command dispatcher
Prerequisites
Python 3.6 or higher

No external dependencies required (uses only Python standard library)

Installation
Clone or download this repository

Navigate to the project directory:

bash
cd "Daily Habit Tracker - Project 1"
Usage
Running the Application
From the project root directory, run:

bash
python main.py
Available Commands
track - Track your habits for today

add - Add habits to your tracking list

remove - Remove habits from your tracking list

streaks - View your current habit streaks

exit - Exit the application

Example Workflow
First Time Setup

text
> python main.py
Welcome to the Daily Habit Tracker!

Main Menu:
 - track
 - add
 - remove
 - exit
 - streaks

> add
Available habits to add:
 - study
 - exercise
 - meditate
 - code
Enter the name of the habit: code
Daily Tracking

text
> track
Did you complete the habit 'code' today? (yes/no): yes
Your habit tracking for today has been saved.
View Your Progress

text
> streaks
Your current habit streaks are:
 - code: 5 day(s)
Default Habits
The tracker comes with these default habits:

study

exercise

meditate

code

You can add unlimited custom habits using the add command.

Data Storage
All data is stored in JSON files:

habits.json - Your habit lists (default, custom, tracking)

tracking.json - Daily completion records by date

Tips for Success
- Track your habits at the same time each day

- Start with 1-3 habits to build consistency

- Check your streaks regularly for motivation

- Don't break the chain - even 5 minutes counts!

Troubleshooting
Issue: "File not found" errors
Solution: Make sure you're running python main.py from the project root directory (where main.py is located)

Issue: Invalid command errors
Solution: Only type the command names (track, add, remove, streaks, exit) at the prompt, not full file paths

Future Enhancements
Potential features for future versions:

 Data visualization (charts/graphs)

 Weekly/monthly summaries

 Habit completion percentages

 Export data to CSV

 Set habit goals and reminders

Author
Ujjwal Babu Bhatta

License
This project is open source and available under the MIT License.

Acknowledgments
Built as Project 1 of a 50-project challenge to learn Python and software development.

Start building better habits today