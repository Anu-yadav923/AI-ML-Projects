import random

print("welcome to Guessing Game!!")

Difficulty_level = int(input("choose difficulty level between 1 to 3 : "))

if Difficulty_level == 1:
    Secret_number = random.randint(1,10)
elif Difficulty_level == 2:
    Secret_number = random.randint(1,50)

else :
    Secret_number = random.randint(1,100)

attempts = 0
won = False

while attempts < 5:
    guess_number = int(input("Guess a number: "))
    attempts += 1

    if guess_number == Secret_number:
        print("yee!! You guessed the correct number!")
        print("attempts : ", attempts)
        won = True
        break
    elif guess_number > Secret_number:
        print("Too high, Guess Smaller number")
    else:
        print("Too low, Guess Larger number.")

if won == False:
    print("Game Over")
    print(f"correct Number was : {Secret_number}")