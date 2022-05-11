import random


def is_valid(number):
    while number.isdigit() == False:
            print("The guess must be a whole number")
            number = input(">")
    while int(number) < 1 or int(number) > 10:
        print("The guess must be between 1 and 10")
        number = input(">")
    return number


current_high_score = ""

print("What is your name?")
name = input(">")

while True:
    number = random.randint(1, 10)
    print(f"Would you like to play the number guessing game, {name}? Please only enter 'yes' or 'no'")
    y_n = input(">").lower()

    while y_n != "yes" and y_n != "no":
        print("Please only enter 'yes' or 'no'")
        y_n = input(">")

    if y_n == "yes":
        print("What number do you guess? The guess must be a whole number between 1 and 10")
        guess = input(">")
        guess = is_valid(guess)
        
        while int(guess) != number:
            print(f"Wrong guess! Try again, {name}")
            print("What number do you guess? The guess must be a number between 1 and 10")
            guess = input(">")
            guess = is_valid(guess)

        print(f"You guessed it! the number was {str(number)}")

    elif y_n == "no":
        print(f"Bye, {name}!")
        break
    

