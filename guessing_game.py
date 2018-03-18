import random

num = random.randrange(0, 10)

#print(num)

while True:
    guess = int(input("What's your guess? "))
    if guess == num:
        print("You guessed it correctly!")
        break
    elif guess > num:
        print("You guessed too high!  Try again!  ")
    else: print("You guessed too low!  Try again!  ")

