from orc import Orc
from player import Player



player1 = Player()
player1.assignName()
player1.assignPlayerWeapon()
player1.character_deaths()

orc1 = Orc()
orc1.assignOrcName()
orc1.assignOrcWeapon()
orc1.character_deaths()



#Encounter
print((player1.name ) + " is adventuring in the woods.")
print(("Suddenly an Orc named " + (orc1.name) + " jumps out at " + ((player1.name))))
print((orc1.name) + " cracks their knuckles, looks at " + (player1.name) + " and grunts 'square go?' " )

#Idea : Turn all of this code into a class that can be called when there is a battle in the story

#battle is initiated
while True: 
    battle_begin = str(input("Will you fight " + (orc1.name) + " ?\n |Aye/Naw| \n"))

#player attack
    if battle_begin in ('aye', 'Aye', 'Yes', 'yes'):
        print((player1.name) + " looks " + (orc1.name) + " in the eyes and shouts back 'meer then'! " )
        print((player1.name) + " takes out their sword and swings at " + (orc1.name) + " it hits doing |" + str(player1.atk) + "| dmg. " )
        orc1.hp -= player1.atk

#orc death    
        if orc1.hp <= 0:
            print((orc1.name) + str(orc1.deaths))
            break

#orc attack
        print("Orc HP : |" + str(orc1.hp) + "|")
        print((orc1.name) + " hits " + (player1.name) + " on the head with their " + (orc1.weapon) + " it hits doing |" + str(orc1.atk) + "| dmg. ")
        player1.hp -= orc1.atk 
        print("Player HP : |" + str(player1.hp) + "|")
        
#player death
        if player1.hp <= 0:
            print((player1.name) + (player1.deaths))
            break
 
#fast run away    
    elif battle_begin in ('Naw', 'No', 'no', 'naw'):
        print((player1.name) + " quickly ran away...")
        break

#run away
    else:
        print((player1.name) + " ran away...")
        break