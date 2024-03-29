class Room():
    """Initialization for rooms"""
    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self.item = None

    """Gets room name"""
    def get_name(self):
        return self.name

    """Gets room description"""
    def get_description(self):
        print(self.description)

    """Sets room description"""
    def set_description(self, room_description):
        self.description = room_description

    """Sets linked room(s)"""
    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link

    """Gets character in room"""
    def get_character(self):
        return self.character

    """Sets character in room"""
    def set_character(self, new_character):
        self.character = new_character

    """Gets item in room"""
    def get_item(self):
        return self.item

    """Sets item in room"""
    def set_item(self, item_name):
        self.item = item_name

    """Prints room name, description and room exits"""
    def get_details(self):
        print("The " + str(self.get_name()))
        print("----------------------")
        print(self.description)
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print("The " + room.get_name() + " is " + direction)

    """Moves between rooms"""
    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You cannot move in this direction.")
            return self
