low = 0
high = 100
feedback = ""
print("Please think of a number between 0 and 100!")
while (feedback != "c"):
    guess = int((low+high)/2)
    print("Is your secret number " + str(int(guess)))
    feedback = input("""Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. """)
    if (feedback == 'l'):
        low = guess
    elif (feedback == 'h'):
        high = guess
    elif (feedback == 'c'):
        print ('Game over. Your secret number was: ' + str(guess))
    else:
        print ('Sorry, I did not understand your input.')
