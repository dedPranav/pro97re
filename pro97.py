import random
print("Guess The Number!")
num= random.randint(1,9)
tries = 0
print("Guess a number between 1 - 9")
while tries<3:
    guess = int(input("Enter your guess: "))
    if guess == num:
        print("You guessed the number!")
    elif(guess<num):
        print("You guessed too low")
    else:
        print("You guessed too high")
    tries=tries+1
if tries==3:
    print("You lost, try again. The number was: ", num)
