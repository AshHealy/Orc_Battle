#all character info


from character import Character
import random

class Player(Character):
#name assignment
    def assignName(self):
        player_name = ["Brad", "Link", "Dorris", "The Final Pam"]
        self.name = random.choice(player_name)

#weapon assignment 
    def assignPlayerWeapon(self):
        player_weapon = ["sword", "dagger", "chainsaw", "spoon"]
        self.weapon = random.choice(player_weapon)

#pet assignment
    def assignPlayerPet(self):
        player_pet = ["Dog", "Cat", "Alligator", "Dragon"]
        self.pet = random.choice(player_pet)

    

         
 
