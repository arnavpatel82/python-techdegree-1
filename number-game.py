import random


current_high_score = ""

print("What is your name?")
name = input(">")
print(f"Welcome to the number guessing game, {name}")

number = random.randint(1, 10)