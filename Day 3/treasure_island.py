print('''
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
  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
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

#Write your code below this line 👇
print("To your left you have the main entrance to the temple with the treasure, to your right you have a hidden side entrance.")
choice1 = input('Type "left" or "right"\n').lower()

if choice1 == "left":
  print("\nAs you enter the temple, you see a stone golem guarding the treasure chamber.")
  choice2 = input('Type "fight" to fight the golem. Type "sneak" to sneak around him unseen.\n').lower()
  
  if choice2 == "sneak":
    print('''
You manage to dodge the golem and arrive at the treasure chamber, where you find three doors.
The first door has the text "fire" engraved above it.
The second has the text "air" instead.
And the third, "earth".
    ''')
    choice3 = input('Type "fire", "air" or "earth" to open the corresponding door.\n').lower()
    
    if choice3 == "fire":
      print("When you open the door, a wall of fire engulfs you. You are toast, Game Over.")
    elif choice3 == "earth":
      print("When you open the door, a mountain of dirt and stone falls ontop of you. You get squished, Game Over.")
    elif choice3 == "air":
      print("When you open the door, a strong wind buffets you. After enduring it, you go into the room to find the treasure! You Win!")
    else:
      print("Wrong command, start again.")
      
  elif choice2 == "fight":
    print("The golem overpowers you. Game Over.")
  else:
    print("Wrong command, start again.")
    
elif choice1 == "right":
  print("You activate a hidden spike trap and fall into it. Game Over.")
else:
  print("Wrong command, start again.")