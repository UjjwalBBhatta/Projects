import json
from src.add_expenses import add_expense
from src.delete_expense import delete_expense
from src.daily_expense import daily_expense
from src.custom_time_expense import timeframe_expense
command_functions ={
    'add': add_expense,
    'delete': delete_expense,
    'today': daily_expense,
    'interval': timeframe_expense,
    'exit': exit
}

def handle_user_input(command):
    """This function handles user input commands and calls the corresponding functions.
    It maps user commands to their respective functions for adding, deleting, and viewing expenses."""
    function = command_functions.get(command)
    if function:
        function()
    else:
        print("Invalid command. Please try again.")

