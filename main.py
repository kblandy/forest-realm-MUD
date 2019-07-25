from character import Character, Enemy, Friend
from room import Room
from item import Item

# ROOMS

parlor = Room("Parlor")
parlor.set_description("\nPerhaps once a lovely entrance, the Venetian tile is cracked now,\nand a stained glass skylight above is shattered, letting in rain and overgrowth of vines.")

kitchen = Room("Kitchen") #gives the object within Room blueprint(class) a name!
kitchen.set_description("\nA dank and dirty room buzzing with flies.")

dining_hall = Room("Dining Hall")
dining_hall.set_description("\nA long, narrow room with a mahogany table and fine china, covered in dust.")

ballroom = Room("Ballroom")
ballroom.set_description("\nTowering ceilings and flaking gold and white paint.  \nFootsteps in the dust hint at the dancers that once were here.")



parlor.link_room(kitchen, "east")
parlor.link_room(dining_hall, "west")

kitchen.link_room(dining_hall, "south")

dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")

ballroom.link_room(dining_hall, "east")

# ENEMY! #

dave = Enemy("Dave", "A zombie who smells of rotting flesh.")
dave.set_conversation("I have a fascinating hunger for brains. Do you have any?")
dave.set_weakness("brain")
dining_hall.set_character(dave) #puts dave in the dining_hall!

borris = Enemy("Borris", "A zombie crawling about the floor, gnashing large, crooked teeth.")
borris.set_conversation("I am absolutely STARVING and you look TASTY!")
borris.set_weakness("brain")
kitchen.set_character(borris)

# Add item(s) to room

brain = Item("brain")
brain.set_description("A wet and wriggling brain.  Looks like zombie food.")
dining_hall.set_item(brain)

quartz = Item("quartz")
quartz.set_description("A huge crystal ball!  It is full of inclusions and very dazzling.")
kitchen.set_item(quartz)

# Add a new character

catrina = Friend("Catrina", "A happily lost treasure-hunter with a fondness for quartz.")
catrina.set_conversation("'Hello, there!  I am looking for a large quartz crystal.  Have you seen it?'")
catrina.set_item_give("quartz")
ballroom.set_character(catrina) #puts catrina in the ballroom



##### CURRENT ROOM #####
current_room = parlor
backpack = [] #empty, as you find items, they will go in backpack

dead = False
while dead == False:
    
    print("\n")
    current_room.get_details()
    print("\n")

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe() 

    item = current_room.get_item()
    if item is not None:
        item.describe()

    command = input("> ")

    if command in ["north", "south", "east","west"]:
        # move in the given direction
        current_room = current_room.move(command)
    elif command == "talk": # talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            inhabitant.talk() 
    elif command == "fight":
        if inhabitant is not None and inhabitant is not Friend: 
            print("What will you fight with?")
            fight_with = input()

            if fight_with in backpack:
                print("You used the ", fight_with, "!")
                if inhabitant.fight(fight_with) == True:
                    current_room.set_character(None) #eliminates the character from the room
                    print(inhabitant.name, "has been subdued and is no longer a threat!") 
                    if inhabitant.get_defeated() == 2: # number of enemies slain
                        print("You have defeated all enemies!")
                else:
                    print("You are doomed to similar fate as the other zombies in this House.")
                    print("####### GAME OVER #######")
                    dead = True   
            else:
                print("You don't have a ", fight_with)
        else:
            print("There is no one here to fight with.")  

    elif command == "wave":
        if inhabitant == None:
            print("There is no one here to wave to.")
        elif isinstance(inhabitant, Enemy):
            print(inhabitant.name, "begins moving towards you.", inhabitant.name, "does not look very friendly...")    
        else:
            inhabitant.wave()

    elif command == "take":
        if item is not None:
            print("You put the ", item.get_name() + " in your backpack.")
            backpack.append(item.get_name())
            current_room.set_item(None)
        else:
            print("There is nothing in this room to take!")

    elif command == "give":
        if inhabitant is not None: 
            print("What do you want to give to ", inhabitant.name, "?")
            give_item = input()

            if give_item in backpack:
                if inhabitant.give(give_item) == True: #boolean from give function!
                    # Can't figure out how to remove give_item from backpack..............
                    print("You've won the game!")
                    dead = True #ends the loop
                else:
                    pass
            else:
                print("You don't have a ", give_item, "!")
        else:
            print("There is no one here to give anything to.")  

    else:
        print("Invalid command")            


    
