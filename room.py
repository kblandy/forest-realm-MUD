class Room():
    def __init__(self, room_name): # __init__ initializes or CREATES the object
        self.name = room_name
        self.description = None #note, you can put "none" here to add parameters later
        self.linked_rooms = {} #dictionary for linking rooms, look below for link method
        self.character = None
        self.item = None
        self.flags = []

    def set_flags(self, flag):
        self.flags.append(flag)   #dark, haunted, etc, will put it into flag[] 
       
    def is_dark(self):
        if "dark" in self.flags:
            return True
        else:
            return False    

    def is_locked(self):
        if "locked" in self.flags:
            return True
        else:
            return False        

# character set
    def set_character(self, new_character):
        self.character = new_character
# character get
    def get_character(self):
        return self.character       
# description set
    def set_description(self, room_description): #
        self.description = room_description # sets the description function for later use in main
# description get
    def get_description(self):
        return self.description # will "get" the description that is set
# getters and setters for room
    def get_name(self):
        return self.name    
    def set_name(self, room_name):    
        return self.name

    # Getters and setters for item
    def get_item(self):
        return self.item

    def set_item(self, item_name):
        self.item = item_name

    def describe(self): # will print the room's description!
        print(self.description)        

    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link
        #print(self.name + "linked rooms:" + repr(self.linked_rooms)) to see what rooms are linked to the indicated room

    def get_details(self): #will print everything in a nice, ordered way.
        print("\n" +('=' *(4 +len(self.name))))
        print("|", (self.name), "|")  # will print the room's name
        print('=' *(4 +len(self.name)))
        print(self.description) # will print out the room's description
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print("\nThe " + room.get_name() + " is " + direction)

