import random
import sys
while True:
    try:
        max_no=int(input("Level: "))
        if max_no < 1: continue
    except:
        continue
    else:
        break

random_no = random.randint(1,max_no)
while True:
    try:
        guess = int(input("Guess: "))
        if guess > max_no or guess < 1:
            continue
        else:
            if guess < random_no:
                print("Too small!")
            elif guess > random_no:
                print("Too large!")
            else:
                break
    except:
        continue

sys.exit("Just right!")