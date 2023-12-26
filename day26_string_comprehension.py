numbers = [1,2,3] 
new_list = []
for num in numbers:
    add_1 = num + 1
    new_list.append(add_1) 

#list comprehension
new_list = [num+1 for num in numbers] 

#string as a list
name = "Simona"
letter_list = [letter for letter in name]

#range as a list
range_list = [n*2 for n in range(1,5)]

#conditional list comprehension
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
short_names = [name.upper() for name in names if len(name)>4] 

# dictionary comprehension
import random 
student_grades = {name: random.randint(1,100) for name in names}

passed_student = {student:grade for student, grade in student_grades.items() if grade>=60}