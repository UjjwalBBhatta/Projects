import json
from src.tracking import track_habits
from src.user_habits import user_habits
from src.streak_counter import streak_counter
command_functions = {
    "track": track_habits,
    "add": user_habits,
    "remove": user_habits,
    "exit": exit,
    "streaks": streak_counter
}
def handle_user_command(command):
    func = command_functions.get(command)
    if func:
        func()
    else:
        print("Invalid command. Please enter 'track', 'add', 'remove', or 'exit'.")