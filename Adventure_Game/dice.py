import random

class Dice():

    def dice(self):
        self.d20 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        self.d12 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        self.d10 = [1, 2, 3, 4, 5, 6,7, 8, 9, 10]
        self.d6 = [1, 2, 3, 4, 5, 6]
        self.d4 = [1, 2, 3, 4]
        self.d2 = [0, 1]
        print(random.choice(self.d20))

    def roll(self):
        print(random.choice(self.d20))

    def test(self):
        print("Hello world!")
