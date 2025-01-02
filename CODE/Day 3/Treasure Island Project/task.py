print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
path = input("You see a path, do you want to go left or right?\n").capitalize()
if path == "Left":
     print("You have chosen the left path, and have arrived at a river bank.\n")
     river = input("\tDo you want to swim or wait for a boat?\n").capitalize()
     if river == "Wait":
         print("A boat arrives to take you across the river. You find three doors once you land.\n")
         door = input("\tPlease choose the door you wish to pass through: Red, Blue or Yellow\n").capitalize()
         if door == "Yellow":
             print("You have found the treasure. \nYOU WIN")
         elif door == "Red":
             print("You fall into a volcano. \nGAME OVER")
         elif door == "Blue":
             print("You enter a jungle, as you do you encounter a group of vicious beasts. \nGAME OVER")
         else:
             print("Wrong move, lightning strikes you. \nGAME OVER")
     elif river == "Swim":
         print("You jump into the water eager to swim across. As you start swimming you encounter some piranha. \nGAME OVER")
     else:
         print("Wrong move, lightning strikes you. \nGAME OVER")
elif path == "Right":
    print("As you move right, the ground cracks apart and you fall into a hole. \nGAME OVER")
else:
    print("Wrong move, lightning strikes you. \nGAME OVER")