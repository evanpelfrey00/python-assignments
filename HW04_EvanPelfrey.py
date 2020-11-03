#Exercise 1
months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'octo', 'nov', 'dec']
for month in months:
    if month[0] == 'j':
        print(month)
#Exercise 2
integers = list(range(100))
for divisable in integers:
    if divisable % 10 ==0:
        print(divisable)        
#Exercise 3
horton = "A person's a person, no matter how small."
vowels = "aeiouAEIOUI"
for vowel in horton:
    for x in vowels:
        if vowel == x:
            print(vowel)
#Exercise 4
word = input('Word?')
y = 'False'
for i in range(len(word)-1):
    if word[i] == word[i + 1]:
        y = 'True'
print(y)
#Exercise 5
words = ['poop', 'ity', 'scoop', 'whoop', 'diddy', 'scoop']
total_length = 0
for word in words:
    total_length += len(word)
average = total_length / len(words)
print(average)

