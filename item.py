class Item():

    # Constructor
    def __init__(self, item_name):
        self.name = item_name
        self.description = None

    # Sets item description
    def set_description(self, item_description):
        self.description = item_description

    # Gets item name
    def get_item_name(self):
        return self.name

    # Gets item description
    def get_item_description(self):
        print(self.description)

    # Looks at item
    def look_at(self):
            print("You look at " + str(self.get_item_name()) + ".")
            self.get_item_description()
