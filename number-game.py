import random


def is_valid(number):
    while True:
        if number.isdigit() == False:
                print("The guess must be a whole, non-negative number")
                number = input(">")
                continue
        elif int(number) < 1 or int(number) > 10:
                print("The guess must be between 1 and 10")
                number = input(">")
                continue
        else:
            break
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
        if bool(current_high_score) == False:
            print("High score: N/A")
        else:
            print(f"High score: {str(current_high_score)}")

        print("What number do you guess? The guess must be a whole number between 1 and 10")
        guess = input(">")
        guess = is_valid(guess)
        
        count = 1
        while int(guess) != number:
            print(f"Wrong guess! Try again, {name}")
            if int(guess) > number:
                print("(hint: your guess was greater than the number)")
            elif int(guess) < number:
                print("(hint: your guess was less than the number)")
            print("What number do you guess? The guess must be a number between 1 and 10")
            guess = input(">")
            guess = is_valid(guess)
            count = count + 1

        print(f"You guessed it! the number was {str(number)}")
        print(f"total guesses: {str(count)}")

        if bool(current_high_score) == False:
            current_high_score = count
            print("New high score!")

        elif count < current_high_score:
            current_high_score = count
            print("New high score!")



    elif y_n == "no":
        print(f"Bye, {name}!")
        break
    

