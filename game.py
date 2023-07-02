import random
import sys

max_no=input("Level: ")

random_no = random.randint(1,max_no)


while True:
    guess = input("Guess: ")
    if guess < random_no:
        print("Too small!")
    elif guess > random_no:
        print("Too large!")
    else:
        print("Just right")
        sys.exit()
