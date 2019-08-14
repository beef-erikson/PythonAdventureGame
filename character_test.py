from character import Enemy

# Just for testing how creating a new enemy works.

# Enemy - Beef
beef = Enemy("Beef", "A viking slab of meat\n")
beef.describe()
beef.set_conversation("Yes, I'm talking meat. I know it's strange.")
beef.talk()
beef.set_weakness("salad")

# Starts fight
print("What will you fight with?")
fight_with = input()
beef.fight(fight_with)
