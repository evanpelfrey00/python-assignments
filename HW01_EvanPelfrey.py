#Exercise 2
grades = [ 'B', 'C', 'A', 'F', 'F', 'D', 'A', 'D', 'A', 'C' ]
frequency = [grades.count('A'), grades.count('B'), grades.count('C'), grades.count('D'), grades.count('F')]
print(frequency)             
#Exercise 3
#Part a
dog_breeds = ['collie', 'sheepdog', 'Chow', 'Chihuahua']
#Part b
herding_dogs = dog_breeds[:2]
print(herding_dogs)
#Part c
tiny_dogs = dog_breeds[3:5]
print(tiny_dogs)
#Part d
print('Persian' in dog_breeds)
#Exercise 4
words = ['chair', 'table', 'music', 'trash', 'can']
print((len(words[0]) + len(words[1]) + len(words[2]) + len(words[3]) + len(words[4]))/ len(words))

