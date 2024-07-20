import random
import time

def multiplication_problem():
    """Generates a random multiplication problem and returns the answer."""
    num1 = random.randint(1, 5)
    num2 = random.randint(1, 5)
    answer = num1 * num2
    print(f"Solve the problem: {num1} x {num2}")
    return answer

def choose_option(prompt, options):
    """Prompts the user to choose an option."""
    print(prompt)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(options):
                return choice
            else:
                print("Invalid choice. Please choose a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    print("Welcome to the Basketball Game!")
    print("You have the chance to score the game-winning buzzer-beater!")
    
    # First choice
    choice1 = choose_option("You have the ball and the clock is ticking down. What do you do?",
                            ["Take a shot from the three-point line",
                             "Pass the ball to a teammate",
                             "Try to drive to the basket"])
    
    if choice1 != 1:
        print("You made the wrong choice and missed the opportunity. Game over!")
        return
    
    print("Good choice! You have an open shot. Get ready for the final moment...")
    
    # Second choice
    choice2 = choose_option("The defender is closing in. Do you:",
                            ["Take the shot immediately",
                             "Fake a shot and then shoot",
                             "Dribble to create more space"])
    
    if choice2 != 1:
        print("You missed the shot! Better luck next time. Game over!")
        return
    
    print("Perfect shot! But to win the game, you need to solve a multiplication problem.")
    
    # Timer for multiplication problem
    start_time = time.time()
    correct_answer = multiplication_problem()
    
    try:
        user_answer = input("You have 5 seconds to answer: ")
        elapsed_time = time.time() - start_time
        
        if elapsed_time > 5:
            print("Time's up! You didn't answer in time. Game over!")
        elif int(user_answer) == correct_answer:
            print("Congratulations! You scored the game-winning buzzer-beater and answered the problem correctly!")
        else:
            print("Incorrect answer! You missed the chance to win. Game over!")
    except ValueError:
        print("Invalid input. Please enter a number.")

main()
