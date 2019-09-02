# Instructions
  # 1. Convert the following into code that uses a while loop.

  # print 2
  # prints 4
  # prints 6
  # prints 8
  # prints 10
  # prints Goodbye!
i = 2;
while (i <= 10):
  print(i)
  i += 2
print("Goodbye!")

  # 2. Convert the following into code that uses a while loop.

  # prints Hello!
  # prints 10
  # prints 8
  # prints 6
  # prints 4
  # prints 2
i = 10;
print("Hello!")
while (i > 0):
  print(i)
  i -= 2

  # 3. Write a while loop that sums the values 1 through end, inclusive. end is a variable that we define for you. So, for example, if we define end to be 6, your code should print out the result:

  # 21
  # which is 1 + 2 + 3 + 4 + 5 + 6.
end = 6
i = 1
total = 0
while (i <= end):
  total += i
  i += 1
print(total)
