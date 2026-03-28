import random

target = random.randint(1,100)

while True:
    userChoice = input("Guess number between 1 to 100 or Quite(Q):")
    if(userChoice == "Q"):
        break

    userChoice = int(userChoice)
    if(userChoice == target):
        print("Congratulations ! You guessed correct number.")
        break
    elif(userChoice < target):
        print("Sory! Your guess is too low . Please try again... ")
    else:
        print("Sorry ! Your guess is too high . Please try again...")


print("--------GAME OVER--------")