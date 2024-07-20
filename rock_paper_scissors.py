import random

def get_computer_choice():
    """Randomly selects a choice for the computer."""
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """Determines the winner of the round."""
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "user"
    else:
        return "computer"

def play_game():
    """Plays a best out of 3 game of Rock, Paper, Scissors."""
    print("Welcome to Rock, Paper, Scissors!")
    
    user_score = 0
    computer_score = 0
    
    while user_score < 2 and computer_score < 2:
        print("\nNew Round")
        
        # Get user input
        user_choice = input("Enter your choice (rock, paper, or scissors): ").strip().lower()
        
        # Validate user input
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue
        
        # Get computer choice
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        
        # Determine the winner
        result = determine_winner(user_choice, computer_choice)
        
        if result == "tie":
            print("It's a tie! No score changes.")
        elif result == "user":
            user_score += 1
            print("You win this round!")
        else:
            computer_score += 1
            print("Computer wins this round!")
        
        print(f"Score - You: {user_score}, Computer: {computer_score}")

    if user_score == 2:
        print("\nCongratulations! You won the best out of 3!")
    else:
        print("\nSorry, the computer won the best out of 3.")


play_game()
