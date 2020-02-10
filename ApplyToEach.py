'''
Instructions:
Write a procedure called oddTuples, which takes a tuple as input, and returns a
new tuple as output, where every other element of the input tuple is copied,
starting with the first one. So if test is the tuple ('I', 'am', 'a', 'test', 'tuple'),
then evaluating oddTuples on this input would return the tuple ('I', 'a', 'tuple').
'''

def positive(a):
    return abs(a)
applyToEach(testList, positive)

def addOne(a):
    return a + 1
applyToEach(testList, addOne)

def square(a):
    return a**2
applyToEach(testList, square)
