epsilon = 0.01
y = int(input("Square root of: "))
guess = y/2.0
while abs(guess**2 - y) >= epsilon:
  guess -= (((guess**2) - y)/(2*guess))
print("The square root of " + str(y) + " is about " + str(guess))
