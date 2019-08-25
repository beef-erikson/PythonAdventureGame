import rpg

# --Fields--
dead = False
backpack = []

# --Rooms--
# Kitchen details
kitchen = rpg.Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")

# Dining Hall details
dining_hall = rpg.Room("Dining Hall")
dining_hall.set_description("A large wooden table is filled with various moldy food items. " +
    "A terrible stench fills the air.")

# Ballroom details
ballroom = rpg.Room("Ballroom")
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
beef = rpg.Enemy("Beef", "A viking slab of meat.\n")
beef.set_conversation("Yes, I'm talking meat. I know it's strange.")
beef.set_weakness("salad")
dining_hall.set_character(beef)

# Vampire
vampire = rpg.Enemy("Vlad", "A dark sinister figure, pale skinned and with pointed teeth, occupies a dark corner of the ballroom.\n")
vampire.set_conversation("I vant to suck your blood, blaaa!")
vampire.set_weakness("stake")
ballroom.set_character(vampire)

# --Friends--
# Casper
casper = rpg.Friend("Casper", "A friendly ghost")
casper.set_conversation("I would really like a hug.")
kitchen.set_character(casper)

# --Items--
# Salad
salad = rpg.Item("salad")
salad.set_description("A nice caesar salad lays here")
kitchen.set_item(salad)

# Stake
stake = rpg.Item("stake")
stake.set_description("A sharp wodden stake sits quietly on the floor")
dining_hall.set_item(stake)

# --Game Loop--
while dead == False:
    # Room details
    print("\n")
    current_room.get_details()
    
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()
    
    item = current_room.get_item()
    if item is not None:
        item.describe()
    
    # --Commands--
    command = input("> ")
    # Travel
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
    
    # Talk
    elif command == 'talk' and inhabitant is not None:
        inhabitant.talk()
    
    # Fight
    elif command == 'fight' and inhabitant is not None and isinstance(inhabitant, rpg.Enemy):
        print("What will you fight with?")
        fight_with = input()
        
        if fight_with in backpack:
            if inhabitant.fight(fight_with) == True:
                print("You have defeated the enemy.")
                current_room.character = None
            else:
                print("The mighty " + inhabitant.name + " has slain you. You have died a horrible death.")
                dead = True
        else:
            print("You do not have this item...")

        if rpg.Enemy.enemies_defeated == 2:
            print("You have defeated all the enemies!")
            quit()
    
    # Steal
    elif command == 'steal' and inhabitant is not None and isinstance(inhabitant, rpg.Enemy):
        inhabitant.steal()
    
    # Sleep
    elif command == 'sleep' and inhabitant is not None and isinstance(inhabitant, rpg.Enemy):
        inhabitant.sleep()
    
    # Hug
    elif command == 'hug' and inhabitant is not None and isinstance(inhabitant, rpg.Friend):
        inhabitant.hug()
    
    # Take
    elif command == 'take' and item is not None:
        backpack.append(item.name)
        print("You have picked up the " + item.name + ".")
        current_room.set_item(None)

    # Inventory
    elif command == 'inventory':
        for items in backpack:
            print(items)