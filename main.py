# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def startProgram():
    print("Welcome to The game")
    initRoom()

def initRoom():
    print("You wake up in a cell and look around. You're able to escape.")
    print("You can only go one way, South. Type 'South' to go south.")
    while True:
        if input() == 'South':
            helmetRoom()
        else:
            print("Wrong input")

def helmetRoom():
    available_paths = [
        'East', 'North'
    ]
    print("You walk into a room filled with wooden boxes.")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    startProgram()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
