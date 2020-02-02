x = int(input("Square root of: "))
epsilon = 0.01
low = 0.0
high = x
ans = (high + low)/2.0
while abs(ans**2 - x) >= epsilon:
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print("The square root of " + str(x) + " is about " + str(ans))
