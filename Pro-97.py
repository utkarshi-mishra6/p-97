import random
number = random.randint(1,9) 

guess = str(input("Enter a number between 1 and 9 : "))
chances = 0
while chances < 5:
    if (guess == number):
        print("Congratulations YOU WIN !!!!!!")
    elif(guess >= number):
        print("You guess is too high, guess a number lower than " + guess)
    else:
        print("Your guess is too low, guess a number higher than " + guess)

    chances += 1

if(chances >= 5):
    print("YOU  LOST ..... The number is " + number)


