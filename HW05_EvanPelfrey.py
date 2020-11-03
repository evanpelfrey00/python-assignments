#Exercise 1a
def hasFinalLetter(strList, letters):
    '''Given a list of strings, and a string of characters, returns a seperate list of only the strings that end with the those characters'''
    returnList = []
    for i in strList:
        for j in letters:
            if i.endswith(j):
                returnList.append(i)
    return(returnList)
#Exercise 1b
x = ["I", "want", "some", "lasagna"]
vowels = "AEIOUaeiou"
y = hasFinalLetter(x, vowels)
print(y)
x = ["Words", "that", "end", "in", "L", "lol"]
l = "Ll"
y = hasFinalLetter(x, l)
print(y)
x = ["None", "of", "these", "should", "print"]
y = hasFinalLetter(x, l)
print(y)
#Exercise 2a
def isDivisable(maxInt, twoInts):
    '''Given an integer, and a tuple of two integers, returns a list of all the integers from one to the first integer divisable by both of the two integers'''
    returnList = []
    for i in range(1 , maxInt):
        if i % twoInts[0] == 0 and i % twoInts[1] == 0:
            returnList.append(i)
    return(returnList)
#Exercise 2b
x = (2, 5)
y = isDivisable(100, x)
print(y)
x = (2, 3)
y = isDivisable(100, x)
print(y)
x = (3, 5)
y = isDivisable(10, x)
print(y)
#Exercise 3a
def longEnough (words, threshold):
    '''Given a list of strings and an integer, returns a list of the strings that are at least that integer characters long.'''
    returnList = []
    for i in words:
        if len(i) >= threshold:
            returnList.append(i)
    return(returnList)
#Exercise 3b
x = ["The", "New", "Jersey", "Devils", "Are", "Stanley", "Cup", "Champions!"]
y = longEnough(x, 5)
print(y)
x = ["don't", "let", "your", "dreams", "be", "memes"]
y = longEnough (x, 4)
print(y)
x = ["a", "b", "c", "d", "e"]
y = longEnough(x, 2)
print(y)
