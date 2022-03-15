import random
# from dice import Dice

class Character():
   def __init__(self):
        self.rolls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        self.hp = 40 + random.choice(self.rolls)
        self.defend = 5 + random.choice(self.rolls)
        self.atk = 5 + random.choice(self.rolls)
        self.lvl = 0
        self.name = ""

   def character_deaths(self):
        deaths = [" succumbs to their wounds and dies", " falls to their knees and dies", "'s life flashes before their eyes.\nThey find it boring and then they die."]
        self.deaths = random.choice(deaths)

   def character_heath_points(self):
       print("My total health points are : " + str(self.hp))
    
   def character_defence(self):
       print("My defence stat is " + str(self.Def))

   def character_attack(self):
       print("My attack stat is " + str(self.Atk))

