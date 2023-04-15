import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choices = [rock, paper, scissors]
#Write your code below this line 👇
#how to select rock, paper ot scissors with 0, 1 and 2.
choice_user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

choice_comp = random.randint(0, 2)

if choice_user < 0  and choice_user >= 3:  
  print("Please enter 0, 1 or 2, only.")
else:
  print(choices[choice_user])
  print(f"The computer chose:\n{choices[choice_comp]}")
  if choice_user == choice_comp:
    print("It's a draw.")
  else:
    if choice_user == 0 and choice_comp == 1:
      print("\nYou lose.")
    elif choice_user == 0  and choice_comp == 2:
      print("\nYou win.")
    elif choice_user == 1  and choice_comp == 0:
      print("\nYou win.")
    elif choice_user == 1  and choice_comp == 2:
      print("\nYou lose.")  
    elif choice_user == 2  and choice_comp == 0:
      print("\nYou lose.")
    elif choice_user == 2  and choice_comp == 1:
      print("\nYou win.")   

