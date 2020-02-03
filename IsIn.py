'''
We can use the idea of bisection search to determine if a character is in a string, so long as the string is sorted in alphabetical order.

First, test the middle character of a string against the character you're looking for (the "test character"). If they are the same, we are done - we've found the character we're looking for!

If they're not the same, check if the test character is "smaller" than the middle character. If so, we need only consider the lower half of the string; otherwise, we only consider the upper half of the string. (Note that you can compare characters using Python's < function.)

Implement the function isIn(char, aStr) which implements the above idea recursively to test if char is in aStr. char will be a single character and aStr will be a string that is in alphabetical order. The function should return a boolean value.

As you design the function, think very carefully about what the base cases should be.
'''

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    # Base case 1: if aStr is empty, the char cannot be in aStr
    if aStr == '':
        return False

    # Base case 2: if aStr is of length 1, test if aStr and char are equal
    if len(aStr) == 1:
       return aStr == char

    # Base case 3: Test if the character in the middle of aStr equals char
    midIndex = len(aStr)//2
    midChar = aStr[midIndex]
    if char == midChar:
       return True

    # Recursive cases: we cannot immediately determine if char is in aStr
    # Recursive case 1: char is "smaller" than midChar
    elif char < midChar:
        return isIn(char, aStr[:midIndex])

    # Recursive case 2: char is "larger" than midChar
    else:
        return isIn(char, aStr[midIndex:])

print(isIn("a", "apple"))
