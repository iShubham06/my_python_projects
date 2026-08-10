import random


def generate_number(minimum, maximum):

    return random.randint(minimum, maximum)



def guess_number_game():


    print("Welcome to the Number Guessing Game!")

    print(f"You can choose a level- ")
    print("Easy: 1 - 50")
    print("Medium: 1 - 100")
    print("Hard: 1 - 500")

    input_level = input("Choose a level: ")


    if input_level == "Easy":
        minimum = 1
        maximum = 50

    elif input_level == "Medium":
        minimum = 1
        maximum = 100

    elif input_level == "Hard":
        minimum = 1
        maximum = 500

    else:
        print("Invalid level. Please choose Easy, Medium, or Hard.")
        return 0

    number = generate_number(minimum, maximum)

    user_input = int(input(f"Guess a number between {minimum} and {maximum}: "))
    attempts = 1
    
    
    
    while user_input != number:
        if user_input < number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
            
        user_input = int(input(f"Guess a number between {minimum} and {maximum}: "))
        attempts += 1
    
        if user_input == number:
            print(f"Congratulations! You guessed the correct number: {number}")
            print(f"Number of attempts: {attempts}")
    
guess_number_game()