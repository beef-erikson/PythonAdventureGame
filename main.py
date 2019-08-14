from room import Room
from item import Item
from character import Enemy
from character import Friend

# --Fields--
dead = False

# --Rooms--
# Kitchen details
kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")

# Dining Hall details
dining_hall = Room("Dining Hall")
dining_hall.set_description("A large wooden table is filled with various moldy food items. " +
    "A terrible stench fills the air.")

# Ballroom details
ballroom = Room("Ballroom")
ballroom.set_description("This ballroom has seen better days. The once magnificent room is now in shambles; cobwebs " +
    "and broken tiles portray what was once a room filled with dancing, happy people.")

# Link room code
kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

# Sets starting room
current_room = kitchen

# --Enemies--
# Beef
beef = Enemy("Beef", "A viking slab of meat.\n")
beef.set_conversation("Yes, I'm talking meat. I know it's strange.")
beef.set_weakness("salad")
dining_hall.set_character(beef)

# Vampire
vampire = Enemy("Vlad", "A dark sinister figure, pale skinned and with pointed teeth, occupies a dark corner of the ballroom.\n")
vampire.set_conversation("I vant to suck your blood, blaaa!")
vampire.set_weakness("stake")
ballroom.set_character(vampire)

# --Friends--
# Casper
casper = Friend("Casper", "A friendly ghost")
casper.set_conversation("I would really like a hug.")
kitchen.set_character(casper)

# --Game Loop--
while dead == False:
    # Room details
    print("\n")
    current_room.get_details()
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()
    
    # --Commands--
    command = input("> ")
    # Travel
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
    # Talk
    elif command == 'talk' and inhabitant is not None:
        inhabitant.talk()
    # Fight
    elif command == 'fight' and inhabitant is not None and isinstance(inhabitant, Enemy):
        print("What will you fight with?")
        fight_with = input()
        if inhabitant.fight(fight_with) == False:
            print("The mighty " + inhabitant.name + " has slain you. You have died a horrible death.")
            dead = True
    # Steal
    elif command == 'steal' and inhabitant is not None and isinstance(inhabitant, Enemy):
        inhabitant.steal()
    # Sleep
    elif command == 'sleep' and inhabitant is not None and isinstance(inhabitant, Enemy):
        inhabitant.sleep()
    # Hug
    elif command == 'hug' and inhabitant is not None and isinstance(inhabitant, Friend):
        inhabitant.hug()

