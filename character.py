import random

class Character():

    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None
        self.awake = True

    # Describe this character
    def describe(self):
        if self.awake:
            print("\n" + self.name + " is here!" )
            print( self.description )
        else:
            print("\n" + self.name + " is here, fast asleep!")

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        if self.awake:
            if self.conversation is not None:
                print("[" + self.name + " says]: " + self.conversation)
            else:
                print(self.name + " doesn't want to talk to you")
        else:
            print(self.name + " is fast asleep and does not respond.")

    # Fight with this character
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True


class Enemy(Character):

    # Initialization for enemies
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None

    # Sets item weakness
    def set_weakness(self, item_weakness):
        self.weakness = item_weakness

    # Gets item weakness
    def get_weakness(self):
        return self.weakness

    # Starts fight
    def fight(self, combat_item):
        if combat_item == self.weakness:
            print("You fend " + self.name + " off with " + combat_item)
            return True
        else:
            print(self.name + " crushes you, puny adventurer")
            return False

    # Steal ability - 2/3 success chance
    def steal(self):
        rand = random.randint(0, 2)
        if rand < 2:
            print("You have stolen some coin and pocket it before " + self.name + " notices.")
        else:
            print(self.name + " has been alerted to your thievery attempts and smacks you violently.")

    # Sleep ability - 2/3 success chance
    def sleep(self):
        rand = random.randint(0,2)
        if rand < 2:
            print("You have managed to put " + self.name + " to sleep with your incantation")
            self.awake = False
        else:
            print("Your incantation seems to have little effect.")
    

class Friend(Character):
    # Initialization for friends
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.happy = False

    # Hugs
    def hug(self):
        print(self.name + " looks much more happier now.")
        if not self.happy:
            self.happy = True