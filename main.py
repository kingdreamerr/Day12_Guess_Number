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
while not guessed_right_number and lives != 0:
  print(f"you have {lives} attempts remaining to guess the number")
  guess = int(input("Make a guess: "))
    
  if guess == guess_number:
    print("You guessed the right number!")
    guessed_right_number = True
  elif guess < guess_number:
    lives -=1
    print("Too low")
  elif guess > guessed_right_number:
    lives -=1
    print("Too high")
  elif lives == 0:
    print("You have {lives} you lose")