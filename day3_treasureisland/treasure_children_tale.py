print('''
*******************************************************************************
                              -|             |-
         -|                  [-_-_-_-_-_-_-_-]                  |-
         [-_-_-_-_-]          |             |          [-_-_-_-_-]
          | o   o |           [  0   0   0  ]           | o   o |
           |     |    -|       |           |       |-    |     |
           |     |_-___-___-___-|         |-___-___-___-_|     |
           |  o  ]              [    0    ]              [  o  |
           |     ]   o   o   o  [ _______ ]  o   o   o   [     | ----__________
_____----- |     ]              [ ||||||| ]              [     |
           |     ]              [ ||||||| ]              [     |
       _-_-|_____]--------------[_|||||||_]--------------[_____|-_-_
      ( (__________------------_____________-------------_________) )
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
direction_i = input("Where do you want to go? Left or Right? ")
direction = direction_i.lower()
if direction == "left":
  action_i = input("What do you want to do? Swim or wait? ")
  action = action_i.lower()
  if action == "wait":
    door_to_i = input("What door will you open? Red, Yellow or Blue? ")
    door_to = door_to_i.lower()
    if door_to == "red":
      print("Burned by fire. Game Over.")
    elif door_to == "yellow":
      print("You win.")
    elif door_to == "blue":
      print("Eaten by beasts. Game Over.")
    else:
      print("Game Over.")  
  else:
    print("Attacked by trout. Game Over.")
else:
  print("Right into a hole. Game Over.")
