#all orc info
import random
from character import Character

class Orc(Character):
    
#Name Assignment

    def assignOrcName(self):
        orc_name = ["Oog", "Big Man", "Smelly Pits", "Jabba", "Janet"]
        self.name = random.choice(orc_name)
    

#Weapon Assignment
    def assignOrcWeapon(self):
        orc_weapon = ["Club", "Axe", "Bag", "broken banjo"]
        self.weapon = random.choice(orc_weapon)


        

