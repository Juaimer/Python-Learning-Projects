print("Welcome to Treasure Island. Your mission is to find the treasure.")

first_decision = input("Do you wanto to go right or left? ")

if first_decision != "Left":
    print("Fall into a hole.")
    print("Game Over.")

second_decision = input("Do you wanto to Swin or wait? ")

if second_decision != "Swin":
    print("Attacked by trout.")
    print("Game Over.")

third_decision = input("Which door do you want to open Red, Blue or Yellow? ")

if third_decision == "Yellow":
    print("You win!")
elif third_decision == "Blue":
     print("Eaten by beasts.")
     print("Game Over.")
elif third_decision == "Red":
     print("Burned by fire.")
     print("Game Over.")
else:
     print("Game Over.")

