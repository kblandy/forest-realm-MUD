class Character():
    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None
        self.alignment = None
        self.inventory = []

    # Describe this character
    def describe(self):
        print("\n" + self.name + " is here:")
        print(self.description)

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    #inventory get/set
    def set_inventory(self, inventory):
        self.inventory.append(inventory)    

# can change character's alignment, i.e. pirate npc, who will kill you if you try to fight him, 
# but becomes a friendly after receiving quest item        
    #def set_alignment(self, align):
        #self.alignment = align

    #def get_alignment(self):
        #return self.align

    #def alignment(self):
        #if self.align == True:
           #self.character == Npc
        #else:
           #self.character == Enemy        

    # prints a statement from the character, I.e., so and so says "this is what they say"
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    # Fight with this character
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True

class Enemy(Character): #tells python that Enemy class inherits all attributes and methods from Character
    
    enemies_defeated = 0
    
    def __init__(self, char_name, char_description): # Character = superclass of Enemy, Enemy = subclass of Character
        super().__init__(char_name, char_description) # means: To make an Enemy, first make a Character object and then we’ll customise it
        
        self.weakness = None
        self.attack_strength = None
        self.defense_strength = None
        self.weapon = None
        self.weapon_desc = None

# weapon get/set
    def set_weapon(self, weapon):
        self.weapon = weapon

    def get_weapon(self):
        return self.weapon

    def set_weapon_desc(self, weapon_desc):
        self.weapon_desc = weapon_desc

    def get_weapon_desc(self):
        return self.weapon_desc

    def weapon_describe(self):
        print(self.weapon_desc)
             

# weakness get/set
    def set_weakness(self, item_weakness):
        self.weakness = item_weakness

    def get_weakness(self):
        return self.weakness    
#attack strength
    def set_attack_strength(self, attack_strength):
        self.attack_strength = attack_strength

    def get_attack_strength(self):
        return self.attack_strength    

#defense strength

    def set_defense_strength(self, defense_strength):
        self.defense_strength = defense_strength

    def get_defense_strength(self):
        return self.defense_strength

    # Getters and Setters for the enemies_defeated varibale
    def get_defeated(self):
        return Enemy.enemies_defeated

    def set_defeated(self, number_defeated):
        Enemy.emies_defeated = number_defeated    

# fight function
    def fight(self, combat_item):
            if combat_item == self.weakness:
                print("You fend " + self.name + " off with the " + combat_item + "!")
                Enemy.enemies_defeated += 1
                return True
            else:
                pass

    def attack(self):
        print(self.name, "attacks you with their", self.weapon, "for", self.attack_strength, "damage.")   
    




# steal
    def steal(self):
        print("You steal from" + self.name)
        # how will you decide what this character has to steal?

class Npc(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.feeling = None

    def wave(self):
        print(self.name + " waves back! " + self.name + " seems friendly.")    

    def set_give(self, give_item):
        self.give_item = give_item

    def get_give(self):
        return self.give_item

    # setters/getters for item_give
    def set_item_give(self, item_give):
        self.item_give = item_give

    def get_item_give(self):
        return self.item_give

    def give(self, special_item):
        if special_item == self.item_give:
            print("You give the " + special_item + " to " + self.name + "!")
            return True
        else:
            print(self.name + " does not want a " + special_item + ". Maybe try a different item?")
            return False    
    
              