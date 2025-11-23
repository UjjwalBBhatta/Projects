import json
from datetime import date, timedelta

def streak_counter():
    """
    Calculate and display current streaks for each tracked habit.
    """
    try:
        with open("tracking.json", "r") as f:
            tracking_data = json.load(f)
        with open("habits.json", "r") as f:
            habit_data = json.load(f)
            tracking_habits = habit_data.get("tracking", [])
        if not tracking_habits:
            print("No habits are being tracked. Please add habits to track first.")
            return
        streaks = {habit: 0 for habit in tracking_habits}
        today = date.today()
        for habit in tracking_habits:
            current_streak = 0
            day_counter = 0
            while True:
                check_date = (today - timedelta(days=day_counter)).isoformat()
                tracking_for_day = tracking_data.get(check_date, {})
                # Adjust this logic to how you save: "yes"/"no" or True/False
                if habit in tracking_for_day:
                    if tracking_for_day[habit] in [True, "yes"]:
                        current_streak += 1
                    else:
                        break
                else:
                    break
                day_counter += 1
            streaks[habit] = current_streak
        print("Your current habit streaks are:")
        for habit, streak in streaks.items():
            print(f" - {habit}: {streak} day(s)")
    except FileNotFoundError:
        print("tracking.json or habits.json file not found.")
    except json.JSONDecodeError:
        print("Error decoding JSON from tracking.json or habits.json.")
    except Exception as e:
        print(f"An error occurred: {e}")
