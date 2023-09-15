# Secret Agent Adventure Game
# by Alex Hadwen-Bennett

generalActions = "Your ability to move is limited.\nGeneral movement is as follows: "

# defines the rooms in the game with SHORT descriptions.
walls = {
    "Front Wall": "Puzzle 1 short description",
    "Back Wall": "Puzzle 2 short description",
    "Left Wall": "Puzzle 3 short description",
    "Right Wall": "Puzzle 4 short description",
}

# defines the walls long description after interaction
wallDescription = {
    "Front Wall": "Puzzle 1 LONG description",
    "Back Wall": "Puzzle 2 LONG description",
    "Left Wall": "Puzzle 3 LONG description",
    "Right Wall": "Puzzle 4 LONG description",
}

# defines the exits that each room has and which room the exits lead to
# optionally you can define an object that must be in the inventory in
# order to move through the exit.
# exits={"Street":{"east":["Lobby"]},
#        "Lobby":{"west":["Street"],"north":["Lift"]},
#        "Lift":{"south":["Lobby"],"up":["1st Floor","KeyCard"]},
#        "1st Floor":{"north":["Lift"]}}

# defines the objects that are present in each room.
# interactible objects
objects = {"Front Wall": [], "Back Wall": [], "Left Wall": [], "Right Wall": []}

# defines objects that hide other objects and must be move to reveal them.
# hidden={"WelcomeMat":"KeyCard"}
hidden = {}

# creates an empty list to store the inventory.
inventory = []


# outputs the details for a room including non-hidden objects.
def roomDetails(wall):
    print("\nLooking at:", wall, "-", walls[wall])
    if len(objects[wall]) > 0:
        print("Objects:")
        for object in objects[wall]:
            if object not in hidden.values():
                print(object)


# moves an object that is hiding another object.
def move(object, room):
    if object in hidden and object in objects[room]:
        print("You have moved", object, "and revealed:", hidden[object])
        del hidden[object]
    else:
        print("It isn't possible to move this object")


# allows the user to add an object to their inventory.
def collect(object, room):
    if object in objects[room]:
        inventory.append(object)
        print(object, "has been added to your inventory.")
    else:
        print("It isn't possible to add this object to your inventory.")


# look at wall and interact with it to get the long description
def interact(room):
    if room in wallDescription:
        print(wallDescription[room])
    else:
        print("No details about this wall available")


# outputs the welcoming message to the user.
print(
    "\nThe year was 1956, and the world had fallen into a desolate state of disrepair. The remnants of once-great cities lay in ruins, and a pervasive sense of longing for a bygone era of retro-futuristic dreams hung in the air. I found myself trapped inside a cubical spaceship, an anachronistic relic from a time when humanity believed in the promise of endless technological advancement."
)

print(
    "\nMy name was Alex, and I was alone in this metallic prison, surrounded by flickering control panels and the distant echoes of forgotten voices. The dimly lit cockpit bore witness to the spaceship's deteriorating condition, a haunting reminder of the world's collapse beyond its walls."
)

print(
    "\nI knew I had a mere thirty minutes to unlock the hatch and make my way out of this metallic prison."
)

print(
    "\nI knew I had a mere thirty minutes to unlock the hatch and make my way out of this metallic prison."
)

print(
    "\nI knew I had a mere thirty minutes to unlock the hatch and make my way out of this metallic prison."
)

# sets the starting room and displays its details.
currentRoom = "Front Wall"
roomDetails(currentRoom)

# allows the user to enter a command and takes the appropriate action.
while True:
    command = input(": ")
    command = command.split()
    if command[0].lower() == "go":
        currentRoom = go(command[1].lower(), currentRoom)
    elif command[0].lower() == "move":
        move(command[1], currentRoom)
    elif command[0].lower() == "collect":
        collect(command[1], currentRoom)
    elif command[0].lower() == "interact":
        interact(currentRoom)
    else:
        print("I'm sorry I didn't understand that command.")
