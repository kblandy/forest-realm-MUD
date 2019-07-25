from character import Character, Enemy, Npc
from room import Room
from item import Item
import sys
import os
import time

### PLAYER STATS ###

inventory = []
health = 20
gold = 20   

### SETTING UP ROOMS ###

# FOREST ROOMS
forest = Room("Forest")
forest.set_description("\nForest Description here")

temple = Room("Temple") #gives the object within Room blueprint(class) a name!
temple.set_description("\nTemple Description here")

river = Room("River")
river.set_description("\nRiver Description here")

# SEA ROOMS
sea = Room("Sea")
sea.set_description("\nSea Description here")

ship = Room("Pirate Ship")
ship.set_description("\nSea Description here")

# VILLAGE ROOMS

village = Room("Village")
village.set_description("\nVillage Desc here")

shop = Room("Supply Shop")
shop.set_description("\nSupply Shop desc here")

gate = Room("Castle Gate")
gate.set_description("\nBehind a huge towering gate you can see the towers of a snow-white castle made of marble.  It sounds like there might be a party going on!") #will be unable to access without quest_item


# CASTLE ROOMS

garden = Room("Garden")
garden.set_description("\nBeautiful gardens surround the area, full of exotic plants exuding buttery and floral fragrances.")
garden.set_flags("locked")

castle = Room("Castle")
garden.set_description("\nThe ivory Castle soars to the heavens, covered in angelic statues of robust nude figures.  There is a party going on!")

parlor = Room("Parlor")
parlor.set_description("\nThrough the Castle doors opens up a large parlor where there are already richly-dressed nobles soliciting, laughing, and drinking.")

buffet = Room("Buffet")
buffet.set_description("\nThere are tables full of food dishes that you have never seen before.")

ballroom = Room("Ballroom")
ballroom.set_description("\nColorful skirts swirl to a large group of minstrels playing.")

### LINKING ROOMS ###

# FOREST ROOMS
forest.link_room(temple, "south")
forest.link_room(river, "east")

temple.link_room(forest, "north")

river.link_room(sea, "south")

sea.link_room(village, "south")
sea.link_room(ship, "west")

# VILLAGE ROOMS
village.link_room(shop, "south")
village.link_room(gate, "west")
shop.link_room(village, "north")

# CASTLE ROOMS
gate.link_room(garden, "north")
gate.link_room(village, "south")
garden.link_room(castle, "north")


castle.link_room(parlor, "north")
castle.link_room(buffet, "west")
castle.link_room(ballroom, "east")
castle.link_room(garden, "south")


# ITEMS
party_invite = Item("Party Invite")
party_invite.set_description("A Party Invite on rich parchment stamped wtih the Royal Seal.")

fancy = Item("Fancy Shoes")
fancy.set_description("A pair of sparkling shoes that seem to be made of diamonds, and flash in the light.")


### CHARACTERS ###

###she should probably have fish in her store ha ha ha
molly = Npc("Molly Malone", "A shop keeper who has the same old items, but new gossip every day.")
molly.set_conversation("'Welcome to my shop!'")
shop.set_character(molly)

redbeard = Enemy("Redbeard", "A handsome pirate with a large red beard and suspiciously dazzling shoes.\nHe carries a large blade on his side that is knicked and marred with age.")
redbeard.set_conversation("'Without the secret token, I will not allow you on board.'")
redbeard.set_attack_strength(100)
redbeard.set_defense_strength(100)
redbeard.set_weapon("Pistol")
ship.set_character(redbeard)

borris = Npc("Borris Boreleon", "A stiff guard who takes joy in following orders and has been working for the Royal Family for over twenty years.")
borris.set_conversation("Judging by your clothes, I doubt you have a Party Invitation.  If you don't, you will need to leave or face severe consequence.")
borris.set_item_give(party_invite.name)
gate.set_character(borris)



#### NAME COLLECTION ####

def stutter_text(string):
    for character in string:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(.03)

def stutter_slow(string):
    for character in string:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(1)

def title():
    os.system('cls')
    witch = "[Witch of the Woods]\n"
    print(witch)
    intro1 = "Oh, a stranger!\n"
    stutter_text(intro1)

    intro2 = "What shall I call you?\n"
    stutter_text(intro2)

    player_name = input("> ")
    intro3 = "An absolute pleasure to meet you, " + player_name + ".\n"
    stutter_text(intro3)
    
    intro4 = "It seems that you have awoken to find yourself lost in my mysterious forest..."    
    stutter_text(intro4)
    time.sleep(1.5)

    os.system('cls')

def gold_function(item, price):
    global gold
    gold_message = "You do not have enough gold for that item."
    gold_message2 = "You bought the " + item
    if gold < price:
        print(gold_message)
    elif gold >= price:
        print(gold_message2," for ", price ," gold.")
        gold = gold - price
        print("GOLD remaining: ", gold)  
    else:
        pass



def shop_1():
    global inventory
    shop_owner = "Molly"

    while True:
        a = "Would you like to talk, shop, or leave?"
        print(a)
        response = input("> ")
        
        if response.lower().startswith("t"):
            os.system('cls')
            b = "'I will say this, my shop is not what it used to be.  I used to have so many items, and was busy every day!'\n"
            stutter_text(b)
            time.sleep(1)
            c = "'In fact, you are the first person I have seen in here in two weeks.  Used to be the talk of the town, I did'\n"
            stutter_text(c)
            time.sleep(1)
            d = "\n" + shop_owner + " pauses a moment, and narrows her eyes.\n"
            print(d)
            time.sleep(1)
            e = "1. Ask about the Revolution\n2. Ask about the Town\n"
            print(e)
            response_3 = input("> ")
            if response_3 == "1":
                f = shop_owner + " seems a little nervous.  She walks over to the open door and shuts it, and closes the drapes.\n"
                print(f)
                time.sleep(1.5)
                g = "'This is not a light matter.  I do not think you understand the gravity of standing up to the nobles,\nand for all I know you could be a spy!'\n"
                stutter_text(g)
                time.sleep(2)
                h = "\n'You will have to prove yourself. Go to the castle and bring me back a pair of Fancy Shoes!'\n"
                stutter_text(h)
                time.sleep(1)
                i = "\nDo you accept this quest (y/n) ?\n"
                print(i)
                response_4 = input("> ")
                if response_4.lower().startswith("y"):
                    j = shop_owner + " smiles, her warm eyes twinkling.  She moves behind a curtain by the counter, and rustles about out of sight.\n"
                    print(j)
                    print("When she emerges, she is holding a fine parchment envelope with elegant handwriting and a royal seal.\n")
                    
                    time.sleep(1.5)
                    k = "'I have been saving this for a special occasion.  There is a party tonight at the Castle.  You will need this to complete your quest.'\n"
                    stutter_text(k)
                    inventory.append(party_invite.name) #adds party invite name to list
                    print("\n", party_invite.name , "has been added to your inventory.") #item not showing in inventory
                    shop_1()
                else:
                    shop_1()    
                ####
            elif response_3 == "2":
                print(shop_owner, " tells about the town and of the Pirate Redbeard and his fascination for beautiful shoes.")
                shop_1()    
            
        elif response.lower().startswith("s"): # NEED PROGRAM TO ADD TO INVENTORY 
            os.system('cls')
            print("Items available:")
            store_items = "\n1. Sword 10g\n2. Shield 10g\n3. Wand 15g\n4. Lute 15g\n5. Leave\n"    
            print(store_items)
            response_2 = input("> ")
            if response_2 == "1":
                gold_function("Sword", 10)
                inventory.append("Sword") # should add item to inventory, but maybe write a function to clean this up
            elif response_2 == "2":
                gold_function("Shield", 10)
                inventory.append("Shield")
            elif response_2 == "3":
                gold_function("Wand", 15)    
                inventory.append("Wand")
            elif response_2 == "4":
                gold_function("Lute",15)  
                inventory.append("Lute")  
        else:
            return village.description  #####not really working but working better?

#castle function here
def castle_quest():
    if party_invite.name in borris.inventory:
        garden.flags.remove("locked") # is still saying garden is locked...
        return garden.description
    
    else:
        print("The Gate is locked and you cannot reach the Castle.")   
        return castle.description
    



#title()     

os.system('cls')

current_room = shop
inventory = [] #empty, as you collect items, they go here
body = ["fist"]

#check inventory function
def inventory_check():
    print(inventory[0:]) #prints location, not item names
    #print(item.name for item in inventory)

    #note, needs to show you item.name while also having the item object within list (not a string that happens to be the same as the item.name)
    #need to check if thing is inventory
    #compare by name
    #give the actual object (not string) to character

def char_inventory_check():
    print (borris.inventory[0:])

while health > 0:

    print("\n")
    current_room.get_details()
    print("\n")

    inhabitant = current_room.get_character()
    item = current_room.get_item()

    if inhabitant is not None:
        inhabitant.describe() 


# Shop function    
    if current_room == shop:
        shop_1()        

    if current_room ==  castle:
        castle_quest()

    item = current_room.get_item()
    if item is not None:
        item.describe()

    command = input("> ")

    if command in ["north", "east","south", "west"]: #all place movement here
        if command in current_room.linked_rooms:
            if current_room.linked_rooms[command].is_locked() == True:
	            print ("The ", current_room.linked_rooms[command].name ," is locked and you cannot enter." )
                
            else:
                current_room = current_room.linked_rooms[command]       
        else:
            #current_room = current_room.move(command)
            print("You cannot go that way")

    elif command == "talk": # talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            inhabitant.talk() 

    elif command == "fight":
        if inhabitant is not None and inhabitant is not Npc: 
            print("What will you fight with?")
            fight_with = input()

            if fight_with in inventory or body:
                print("You used your ", fight_with, "!")
                if inhabitant.fight(fight_with) == True:
                    current_room.set_character(None) #eliminates the character from the room
                    print(inhabitant.name, "has been subdued and is no longer a threat!")     
                else:
                    inhabitant.attack() 
                    health = health - inhabitant.attack_strength
                    print("Your health is ", health)
                    if health <= 0:
                        time.sleep(3)
                        print("Press enter to continue...")
                        gameover = input(">")
                        os.system('cls')
                        z = "You have died. Your spirit floats away from your mortal body.  Perhaps you will be reincarnated to finish your journey in another life.\n"
                        stutter_text(z)
                        time.sleep(1.5)
                        print("####### GAME OVER #######")
                        os.system('cls')
         
            else:
                print("You don't have a ", fight_with)
        else:
            print("There is no one here to fight with.")          

    elif command == "give":
            if inhabitant is not None: 
                print("What do you want to give to ", inhabitant.name, "?")
                give_item = input()
                
                if give_item in inventory or give_item in body:
                    if inhabitant.give(give_item) == True: #boolean from give function!
                        # inhabitant.give(give_item)
                        inhabitant.inventory.append(give_item) #should add item to character's inventory   
                        inventory.remove(give_item) #deletes item from user's inventory

                    else:
                        pass
                else:    
                    print("You don't have a ", give_item, "!")
            else:
                print("There is no one here to give anything to.")
                
    elif command == "inventory":
        inventory_check()
        #print(item.name for Item in inventory)

    elif command == "borris": #checks character's inventory
        char_inventory_check()

    else:
        print("Invalid command")    

