import random
computer_selection = random.randint(0, 2) 

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

OPTIONS = [rock, paper, scissors]

user_selection = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scirssors. "))

if user_selection == computer_selection:
    print("Even")
elif user_selection == 0 and computer_selection == 2:
    print(f"You win! \n\n Your selection ${OPTIONS[user_selection]} \n\n  Computer selection {OPTIONS[computer_selection]}")
elif user_selection == 2 and computer_selection == 1:
    print(f"You win! \n\n Your selection ${OPTIONS[user_selection]} \n\n  Computer selection {OPTIONS[computer_selection]}")
elif user_selection == 1 and computer_selection == 0:
    print(f"You win! \n\n Your selection ${OPTIONS[user_selection]} \n\n  Computer selection {OPTIONS[computer_selection]}")
else:
    print(f"You Lost! \n\n Your selection ${OPTIONS[user_selection]} \n\n  Computer selection {OPTIONS[computer_selection]}")
