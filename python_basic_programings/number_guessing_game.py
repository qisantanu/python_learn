# number guessing game in Python
# This is a simple number guessing game where the computer selects a random number
# between 1 and 100, and the user has to guess it.
import random
import time

def number_guessing_game():
  attempt = 0
  print("Welcome to the Number Guessing Game!\n")
  print("Let me first select a number.\n")
  time.sleep(2)  # Simulate thinking time
  print("Selecting...")
  secret_number = random.randint(1, 100)
  time.sleep(2)  # Simulate thinking time
  print("Alright! I have selected a number between 1 and 100. Can you guess it?\n")
  while True:
    guess = input("Enter your guess: ")
    
    if not guess.isdigit():
      print("Please enter a valid number.")
      continue
    
    guess = int(guess)
    attempt += 1
    if guess < secret_number:
      print("Too low! Try again.")
    elif guess > secret_number:
      print("Too high! Try again.")
    else:
      print("Congratulations! You've guessed the number in " + str(attempt) + " attempts!")
      break


number_guessing_game()