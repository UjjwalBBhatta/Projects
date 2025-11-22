import json
from tracking import track_habits
from user_habits import user_habits

command_functions = {
    "track": track_habits,
    "add": user_habits,
    "remove": user_habits,
    "exit": exit
}
def handle_user_command(command):
    func = command_functions.get(command)
    if func:
        func()
    else:
        print("Invalid command. Please enter 'track', 'add', 'remove', or 'exit'.")