# Author : Samridhi Gupta
# Date : 24-12-2024
# Project : Snake,Water,Gun game

# importing random
import random

# defining welcome function
def welcome():
    print("Welcome to Snake,Water,Gun game")

# defining get_user_option function to get user input
def get_user_option():
     return input("Enter your option [Snake,Water,Gun]: ").capitalize()

# defining get_computer_option function to get computer input
def get_computer_option():
    return random.choice(["Snake","Water","Gun"]).capitalize()

# defining determine_winner function to determine the winner
def determine_winner(user_option,computer_option):
    if (user_option == 'Snake' and computer_option == 'Water') or (user_option == 'Water' and computer_option == 'Gun') or (user_option == 'Gun' and computer_option == 'Snake'):
        return "You Win"
        
    elif (user_option == computer_option):
        return "Tie"
    else:
        return "You Lose"

# defining play_game function to play the game     
def play_game():
    choice = 'Y'

    # initializing score
    user_score = 0
    computer_score = 0
    
    # creating a loop
    while choice != 'N':
        user_option = get_user_option()
        computer_option = get_computer_option()
        print("Computer selected option is: ",computer_option)

        # determinig the winner
        result = determine_winner(user_option,computer_option)

        # updating score
        if result == "You Win":
            user_score += 1
        elif result == "Tie":
            pass
        else:
            computer_score += 1

        # printing score
        print("Your score is: ",user_score)
        print("Computer score is: ",computer_score)

        # asking user to play
        choice = input("Do you want to play? Y/N : ").capitalize()

        # ending loop

    # Final score
    print("Your final score is: ",user_score)
    print("Computer final score is: ",computer_score)

    # Checking who is the winner
    if user_score > computer_score:
        print("You are the winner of this game")
    else:
        print("Computer is the winner of this game")


# main function
if __name__ == "__main__":
    welcome()
    play_game()