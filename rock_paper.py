import random

acceptable_choice = ["R", "P", "S"]
print("Ready to play the game of Rock-Paper-Scissors?")
print("Here are the acceptable options \n'R for Rock', \n'P for Paper', \n'S for Scissors' ")


def choice_check():

    user_choice = "123"
    within_option = False

    while user_choice.isalpha() == False or within_option == False:

        selection = input("Pick one of these letters: 'R', 'P', 'S' ")
        user_choice = selection.upper()

        # check for alphabet
        if user_choice.isalpha() == False:
            print("Sorry!!! That is not an alphabet")

        elif user_choice.isalpha() == True:
            if user_choice in acceptable_choice:
                within_option = True
            else:
                print("Invalid option: not within option")

    return(user_choice)


def guesses():

    user_guess = choice_check()
    auto_guess = random.choice(acceptable_choice)

    print(
        f"Player {user_guess} : CPU {auto_guess}")

    if user_guess == auto_guess:
        print("We have a tie !!")

    elif user_guess == "R" and auto_guess == "P":
        print("You Lose !!")

    elif user_guess == "P" and auto_guess == "R":
        print("You Win!!")

    elif user_guess == "P" and auto_guess == "S":
        print("You Lose !!")

    elif user_guess == "S" and auto_guess == "P":
        print("You Win !!")

    elif user_guess == "S" and auto_guess == "R":
        print("You Lose !!")


def gameon_choice():

    game_show = guesses()
    choice = 'wrong'

    while choice not in ['Y', 'N']:

        choice = input(
            "Would you like to play another game? (Y or N) ").capitalize()

        if choice not in ['Y', 'N']:
            print("Sorry, I don't understand, please choose Y or N ")
        while choice == "Y":
            guesses()
            choice = input(
                "Would you like to play another game? (Y or N) ").capitalize()
        break


gameon_choice()
