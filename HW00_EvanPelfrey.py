"""
Evan Pelfrey
CS 100 2018F Section 101
HW 00, Sep 12, 2018
"""
#Exersise 5b
face = 1
limbs = 4
fingers = 10
#Exercise 5c
oneAndQuarter = 1.25
oneAndHalf = 1.5
oneAndThreeQuarters = 1.75
#Exercise 5d
NJIT = "Awesome"
newJerseyDevils = "Good"
newYorkRangers = "Bad"
#Exercise 6, Chapter 1.9, Exercise 1
"""
1. In a print statement, if you leave out one of the parenthesis, Python will not know where the end of what you're printing is. If you leave out both of the parenthesis, Python won't know where the start or end of what it is printing is.
2. If you are trying to print a string, and you leave out one of the quotation marks, Python will treat the one quotation mark as the start of a string, and everything after it would be part of the string. If you leave out both quotation marks, python will think you are trying to print a variable, not a string.
3. If you put a plus before a number, it will treat the number as positive. 2++2 will result in 4, because the first plus sign is an arithemetic operator for addition, and the second plus sign is defining the second 2 as positive.
4. If you use a leading 0, (for example, 02) Python will not see 02 the same way as it sees 2.
5. If you have two values with no operator between them, Python will not known what to do to the values, or how to compare them, so the line will result in an invalid syntax.
"""
#Exercise 6, Chapter 1.9, Exercise 2
"""
1.
secondsInAMinute = 60
42 * secondsInAMinute + 42
2.
kilometersInAMile = 1.61
10 / kilometersInAMile
3.
(42 * secondsInAMinute + 42) / (10 / kilometersInAMile)
(42 + (42 / 60)) / (10 / kilometersInAMile)
(10 / kilometersInAMile) / ((42 + (42 / 60)) / 60
"""
#Exercise 6, Chapter 2.1, Exercise 1
"""
n = 42 is legal because you are assigning a value to the variable n. n - 42 is legal, because if n is represented by the value 42, then 42 - 42 = 0
x = y = 1 is legal because both the variables x and y will be assigned the value 1.
If you add a semicolon to the end of a Python statement, it seemingly does nothing.
If you add a period to the end of a statement, you will get an invalid syntax eror.
If you tried to multiple x and y by typing xy in Python, Python would search for the variable titled xy, and either not find anything, or find what you weren't looking for.
"""
#Exercise 6, Chapter 2.1, Exercise 2
r = 5
radiusFormula = (4/3)*(3.14)*(r**3)
print(radiusFormula)
coverPrice = 24.95
copies = 60
wholesalePrice = (coverPrice * copies * 0.6) + ((copies -1) * 0.75) + 3
print(wholesalePrice)
#Departure time = 6:52 am
timeDepartMinutes = 6*60 + 52
easyPace = 8 + (15/60)
tempoPace = 7 + (12/60)
runTime = (easyPace * 2) + (tempoPace * 3)
arrivalTimeMinutes = timeDepartMinutes + runTime
hour = int(arrivalTimeMinutes // 60)
minutes = int(arrivalTimeMinutes % 60)
print(hour , ':', minutes)



