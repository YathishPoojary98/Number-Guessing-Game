import random

# generate a random number between 1 and 100
number = random.randint(1, 100)

# set the number of tries
tries = 5

# loop through the game
while tries > 0:
    # get the user's guess
    guess = int(input("Guess a number between 1 and 100: "))

    # check if the guess is correct
    if guess == number:
        print("Congratulations! You guessed the number!")
        break
    elif guess > number:
        print("Too high! Guess again.")
    else:
        print("Too low! Guess again.")

    # decrement the number of tries
    tries -= 1
    print("You have", tries, "tries left")

# if the user runs out of tries, the game is over
if tries == 0:
    print("Sorry, you ran out of tries. The number was", number)

