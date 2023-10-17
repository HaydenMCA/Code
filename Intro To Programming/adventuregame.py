# Welcome message
print("Welcome to the Adventure Game!")

# First scenario
print("You find yourself in a dark forest. A mysterious path splits into two.")
print("Which way do you choose? LEFT / RIGHT")

choice1 = input("Your choice: ").strip().upper()

if choice1 == "LEFT":
    # Second scenario
    print("You follow the left path and reach a river.")
    print("You can see a boat nearby, but you hear growling in the bushes.")
    print("What do you do? GET IN BOAT / INVESTIGATE")

    choice2 = input("Your choice: ").strip().upper()

    if choice2 == "GET IN BOAT":
        # Third scenario
        print("You safely cross the river and find a treasure chest on the other side.")
        print("Congratulations, you've won the game!")
    elif choice2 == "INVESTIGATE":
        # Third scenario
        print("You investigate the bushes and find a friendly squirrel.")
        print("It leads you to a hidden path. You're on your way to an adventure!")

    else:
        print("Invalid choice. Please choose from the available options.")

elif choice1 == "RIGHT":
    # Second scenario
    print("You follow the right path and come across a cave entrance.")
    print("There's a torch at the entrance, and you hear strange sounds from inside.")
    print("What's your next move? TAKE TORCH / ENTER CAVE")

    choice2 = input("Your choice: ").strip().upper()

    if choice2 == "TAKE TORCH":
        # Third scenario
        print("You take the torch and enter the cave. It's filled with ancient treasures.")
        print("You've become a legendary explorer!")

    elif choice2 == "ENTER CAVE":
        # Third scenario
        print("You enter the cave, but it's dark, and you can't see anything.")
        print("Suddenly, you feel a presence behind you. You've been caught by a monster!")

    else:
        print("Invalid choice. Please choose from the available options.")

else:
    print("Invalid choice. Please choose from the available options.")

# End of the game
print("Thanks for playing!")
