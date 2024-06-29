##############Guessing Game ##############
import random
from art import logo

def check_answer(guess_number, num_target):
  if guess_num > num_target:
    print("Too high.\nGuess again")
  elif guess_num < num_target:
    print("Too low.\nGuess again")
  else:
    print(f"You got it! The answer was {num_target}.")


EASY_TURN_LEVEL = 10
HARD_TURN_LEVEL = 5
UNDEFINED_LEVEL = 0

def difficult_level():
  game_level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if game_level == "easy":
    return EASY_TURN_LEVEL
  elif game_level == "hard":
    return HARD_TURN_LEVEL
  else:
    return UNDEFINED_LEVEL
    
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

num_list = []
for num in range(1,101): # or num_target = randint(1,100)
  num_list.append(num)
num_target = random.choice(num_list)
# print(num_target)

turns = difficult_level()

guess_num = int(input("Make a guess: "))

is_game_over = False
while not is_game_over:
  if guess_num != num_target and turns != 0:
    check_answer(guess_num, num_target)
    guess_num = int(input("Make a guess: "))
    turns -= 1
    if turns ==0:
      print("You've run out of guesses, you lose!")
      is_game_over = True
    else:
      print(f"You have {turns} attemps remaining to guess the number.")
  else:
    is_game_over = True