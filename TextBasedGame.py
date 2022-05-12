# Trevor Mayo IT140
# Sample function showing the goal of the game and move commands
def show_instructions():
    # print a main menu and the commands
    print("Goblin Text Adventure Game")
    print("Collect 6 items to win the game, or be killed by the goblin.")
    print("Move commands: South, North, East, West")
    print("Add to Inventory: get 'item name'")
    print("Exit the game: exit")


# In this solution, the player’s status would be shown in a separate function.
# You may organize your functions differently.

def main():
    rooms = {
        'Start Room': {'South': 'Box Room'},
        'Box Room': {'North': 'Start Room', 'East': 'Fire Room', 'item': 'Helmet'},
        'Fire Room': {'West': 'Box Room', 'North': 'Cot Room', 'East': 'Chest Room', 'South': 'Shelf Room',
                      'item': 'Sword'},
        'Cot Room': {'East': 'Bone Room', 'South': 'Fire Room', 'item': 'Chaps'},
        'Bone Room': {'West': 'Cot Room', 'South': 'Chest Room', 'item': 'Chainmail'},
        'Chest Room': {'West': 'Fire Room', 'North': 'Bone Room', 'item': 'Shield'},
        'Shelf Room': {'West': 'Goblin Room', 'North': 'Fire Room', 'item': 'Gloves'},
        'Goblin Room': {'exit': 'exit', 'East': 'Shelf Room'}
    }
    print()
    print(
        "You wake up in a cell and look around. The door to the cell is locked.\n"
        "Three feet outside the cell, you see a key dangling from a hook.\n"
        "You grab a stick next to you and attempt to reach the keys. You're able to escape.")
    print("You can only go one way, South. Type 'South' to go south or 'exit' to leave the game")
    print()
    show_instructions()
    gameLoop(rooms)


def gameLoop(allRooms):
    goblin_Killed = False
    rooms = allRooms
    # init room
    curRoom = 'Start Room'
    # init inventory at none
    inventory = []
    print("Available commands:")
    # prints all commands
    for i in rooms[curRoom]:
        if i != "item":
            print(i)
        else:
            print("get " + rooms[curRoom].get(i))

    while True:
        # get input of room
        print()
        choice = input()
        split_string = choice.split()
        # if they type exit, exit program
        if choice == 'exit':
            print("Thanks for playing.")
            exit(1)
        # if the input is two words
        elif len(split_string) == 2:
            # if the command is valid for getting item
            if split_string[0] == 'get' and split_string[1] == rooms[curRoom].get("item"):
                item = rooms[curRoom].get("item")
                if item:
                    if item not in inventory:
                        print("You grab the " + item)
                        inventory.append(item)
                    else:
                        print("You already have the item from this room.")
                else:
                    print("That was an invalid response.")
            else:
                print("That was an invalid response")
        # if the current room has the input as an option
        elif rooms[curRoom].get(choice):
            # switch current room to new room
            curRoom = rooms[curRoom].get(choice)
            # if the room has an item in it
            if rooms[curRoom].get("item"):
                print("You walk into the " + curRoom + " and you see a " + rooms[curRoom].get("item"))
            # if the room is the boss room
            if curRoom == "Goblin Room":
                # if you didnt take all the items
                if len(inventory) < 6:
                    print("The goblin has killed you, you're not strong enough.")
                    print()
                    show_instructions()
                    curRoom = 'Start Room'
                    inventory = []
                else:
                    if goblin_Killed == True:
                        print("You've already killed the goblin, type 'exit' to leave.")
                    else:
                        print("You've killed the goblin, type 'exit' to leave.")
                        goblin_Killed = True
                        if input() == "exit":
                            exit(0)
        # invalid input
        else:
            print("Try again")
        # prints inventory every turn and available commands
        print("Inventory: {}".format(inventory))
        print("Available commands:")
        # prints all commands
        for i in rooms[curRoom]:
            if i != "item":
                print(i)
            else:
                if rooms[curRoom].get("item") not in inventory:
                    print("get " + rooms[curRoom].get(i))


if __name__ == '__main__':
    main()
