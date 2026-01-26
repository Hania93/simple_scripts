print("Welcome to the Treasure Island")
print("Your mission is to find the treasure.")

direction = input("Where do you want to go? Press r - (go right) or l - (go left)").lower()

if direction == "l":
    action = input("Do you want to swim or wait? Press s - (swim) or w - (wait)").lower()

    if action == "w":
        door = input("Which door do you choose? Press r - (red) or b - (blue) or y - (yellow)").lower()

        if door == "b":
            print("You win!")

        elif door == "y":
            print("Eaten by beasts. Game Over.")

        elif door == "r":
            print("Burned by fire. Game Over")

        else:
            print("You lose! Game Over")

    else:
        print("Attacked by trout. Game Over.")

else:
    print("Fall into a hole. Game Over.")

