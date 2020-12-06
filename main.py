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

game_elements = [rock, paper, scissors]
game_elements_name = ["rock", "paper", "scissors"]
print("Welcome to rock, paper, scissors.")
print("Type 0 for rock, 1 for paper, and 2 for scissors.")
user_selection = int(input("Which one would you choose? "))


#For computer's selection
computer_selection = random.randint(0, len(game_elements) - 1)


#Who wins

if user_selection >= 3 or user_selection < 0:
  print("You typed an invalid option.  You lost.")
else:
  print("You selected:")
  print(game_elements[user_selection])
  print(game_elements_name[user_selection])
  print("\n")
  print("The computer selected:")
  print(game_elements[computer_selection])
  print(game_elements_name[computer_selection])
  if computer_selection == user_selection:
    print("It's a draw.")
  elif user_selection == 0:
    if computer_selection == 1:
      print("You lost.")
    else:
      print("You won!")
  elif user_selection == 1:
    if computer_selection == 0:
      print("You win!")
    else: 
      print("You lost.")
  elif user_selection == 2:
    if computer_selection == 0:
      print("You lost.")
    else:
      print("You won!")



