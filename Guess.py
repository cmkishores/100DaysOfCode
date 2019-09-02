import random
i = True
x = random.randint(1,101)
while i:
 
    guess = int(input ("Enter a number: "))
    if (guess<x):
        print(" Guess is less than the number")
    elif (guess>x):
        print(" Guess is greater than the number")
    elif(guess == x):
        print ("You Won! That was a correct guess")
        i = False