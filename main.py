from random import randint
from art import logo

print(logo)
guess_number = randint(0,101)
lives = 0
level = ""
guessed_right_number = False

print("Welcome to the guessing game!")
print("I'm guessing a number between 1 and 100.")
level_chosen = input("Choose a difficulty. type 'easy' or 'hard': ").lower()
if level_chosen == 'hard':
  lives = 5
else:
  lives = 10
