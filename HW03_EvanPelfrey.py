#Exercise 1 and 2
a = 3
b = 4
c = 5
if a < b:
    print('OK')
else:
    print('NOT OK')
if c < b:
    print('OK')
else:
    print('NOT OK')
if a + b == c:
    print('OK')
else:
    print('NOT OK')
if a**2 + b**2 == c**2:
    print('OK')
else:
    print('NOT OK')
#Exercise 3 
color = input('Color?')
line_width = int(input('line width? (number)'))
line_length = int(input('line length? (number)'))
shape = input('shape? (line, triangle, or square)')
import turtle
screen = turtle.Screen()
turtle = turtle.Turtle()
turtle.color(color)
turtle.width(line_width)
if shape == 'line':
    turtle.forward(line_length)
elif shape == 'triangle':
    turtle.forward(line_length)
    turtle.left(120)
    turtle.forward(line_length)
    turtle.left(120)
    turtle.forward(line_length)
elif shape == 'square':
    turtle.forward(line_length)
    turtle.right(90)
    turtle.forward(line_length)
    turtle.right(90)
    turtle.forward(line_length)
    turtle.right(90)
    turtle.forward(line_length)
#Exercise 4
homework = int(input('Homework Percentage'))
homeworkConverted = (homework * 0.1)
officeHours = int(input('Office Hours Percentage'))
officeHoursConverted = (officeHours * 0.04)
midtermOne = int(input('Midterm One Percentage'))
midtermOneConverted = (midtermOne * 0.2)
midtermTwo = int(input('Midterm Two Percentage'))
midtermTwoConverted = (midtermTwo * 0.2)
finalExam = int(input('Final Exam Percentage'))
finalExamConverted = (finalExam * 0.3)
roadmapProjects = int(input('Roadmap Projects Percentage'))
roadmapProjectsConverted = (roadmapProjects * 0.1)
misc = int(input('Misc Percentage'))
miscConverted = (misc * 0.06)
overallGrade = homeworkConverted + officeHoursConverted + midtermOneConverted + midtermTwoConverted + finalExamConverted + roadmapProjectsConverted + miscConverted
print('Overall Grade:', overallGrade)
if (overallGrade >= 85 and finalExam >= 80):
    print('A')
if overallGrade >= 85 and finalExam >= 75 and finalExam <= 80:
    print('B+')
if overallGrade >= 85 and finalExam >= 70 and finalExam <=75:
    print('B')
if overallGrade >= 85 and finalExam >= 65 and finalExam <=70:
    print('C+')
if overallGrade >= 85 and finalExam < 65:
    print('F')
if overallGrade >= 80 and overallGrade < 85 and finalExam >= 80:
    print('B+')
if overallGrade >= 80 and overallGrade < 85 and finalExam >= 75 and finalExam <= 80:
    print('B+')
if overallGrade >= 80 and overallGrade < 85 and finalExam >= 70 and finalExam <=75:
    print('B')
if overallGrade >= 80 and overallGrade < 85 and finalExam >= 65 and finalExam <=70:
    print('C+')
if overallGrade >= 80 and finalExam < 65:
    print('F')
if overallGrade >= 75 and finalExam >= 80:
    print('B')
if overallGrade >= 75 and finalExam >= 75 and finalExam <= 80:
    print('B')
if overallGrade >= 75 and finalExam >= 70 and finalExam <=75:
    print('B')
if overallGrade >= 75 and finalExam >= 65 and finalExam <=70:
    print('C+')
if overallGrade >= 75 and finalExam < 65:
    print('F')
if overallGrade >= 70 and finalExam >= 80:
    print('C+')
if overallGrade >= 70 and finalExam >= 75 and finalExam <= 80:
    print('C+')
if overallGrade >= 70 and finalExam >= 70 and finalExam <=75:
    print('C+')
if overallGrade >= 70 and finalExam >= 65 and finalExam <=70:
    print('C+')
if overallGrade >= 70 and finalExam < 65:
    print('F')
if overallGrade <= 65:
    print('F')
