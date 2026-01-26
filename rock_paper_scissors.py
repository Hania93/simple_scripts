# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

import random

computer_choice = random.randint(0, 2)

user_choice = int(input("What do you choose? Rock - 0, Paper - 1, Scissors - 2 "))

choices_images = [rock, paper, scissors]

if user_choice != '':
    print("Computer chose: ", choices_images[computer_choice])
    print("User chose: ", choices_images[user_choice])

    if computer_choice == user_choice:
        print("It's a tie!")

    elif computer_choice == 0 and user_choice == 1:
        print("You win!")

    elif computer_choice == 0 and user_choice == 2:
        print("Computer win!")

    elif computer_choice == 1 and user_choice == 2:
        print("You win!")

    elif computer_choice == 1 and user_choice == 0:
        print("Computer win!")

    elif computer_choice == 2 and user_choice == 0:
        print("You win!")

    elif computer_choice == 2 and user_choice == 1:
        print("Computer win!")

    else:
        print("You input invalid value. Try again.")










