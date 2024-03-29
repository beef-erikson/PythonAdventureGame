class Item():
    """Initialization for items"""
    def __init__(self, item_name):
        self.name = item_name
        self.description = None

    """Sets item description"""
    def set_description(self, item_description):
        self.description = item_description

    """Gets item description"""
    def get_description(self):
        print(self.description)

    """Gets item name"""
    def get_item_name(self):
        return self.name

    """"Describes item"""
    def describe(self):
        print("The [" + self.name + "] is here - " + self.description)
