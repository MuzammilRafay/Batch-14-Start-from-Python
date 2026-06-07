# Data Types

# Object & Mutability

# everything is object in python

# OBJECT

# every object has it is unique identity
# every object has it is type
# every object has value


# mutable & immutable

# mutable is changeable
# immutable is not changeable

# identity help us to check changeable & not changeable




# Immutable Data Types
# Immutable = Cannot be changed after creation.

# Immutable Data Types are
# 1.Int = 10
# 2.string = "Ali"
# 3.tuple = (1,2)

# Mutable Data Types
# 4.list = [1,2]
# 5.dict = {name:"Ali"}
# 6.set = {1,2}
# 7.Boolean = True False


student_name = "Ali"
course_name = "Python"

print(f"{student_name[0]}")
# print(f"{student_name} is learning {course_name}")
title = "Python Programming"

print(title[:6]) # Python
print(title[7:]) # Programming
print(title[::-1]) #reverse

name = "José"

encoded = name.encode("utf-8")
decoded = encoded.decode("utf-8")

print(encoded)
print(decoded)

print(len(title)) #length 

store = 1

# print(len(store))

#Tuple

week_days = ("Monday", "Tuesday", "Wednesday")
# () parentheses


student = ("Ali", 18, "Python")
name,age,course = student


morning_students = 20
evening_students = 30

morning_students, evening_students = evening_students, morning_students

print(morning_students)
print(evening_students)

#List
# [] 
# square bracket 

students = ["Ali", "Sara"]

students.append("Ahmed") 


students = ["Ali"]
new_students = ["Sara", "Ahmed"]

students.extend(new_students)

print(students)


# insert
# Adds item at a specific index.

students = ["Ali", "Ahmed"]

students.insert(1, "Sara")

print(students)


removed = students.pop()
students.reverse()
students.sort()


print(removed)
print(students)

# List Operators
frontend = ["HTML", "CSS"]
backend = ["Python", "FastAPI"]

skills = frontend + backend

print(skills)

# Multiplication Operator
weekly_classes = ["Python"] * 3

print(weekly_classes)


# Dictionary
# key value

student = {
    "name": "Ali",
    "course": "Python",
    "fee": 3500
}

print(student["name"])
print(student.get("phone","Fallback default value"))
print(student.keys())
print(student.values())
print(student.items())
student.update({"city": "Karachi"})


removed = student.popitem() #remove last item

print(removed)
print(student)



# Set
# object without keys
skills = {"Python", "React", "Python"} #it will remove duplicates

print(skills)

#please check the image

isActive = True
isActive = False


code = bytearray(b"STD001")
code = bytearray(b"OLD_STUDENT")


print(code)

from decimal import Decimal #import libraries
fee = Decimal("3500.50") #3500.50


name = "Ali"
age = 20

print(type(name))
print(type(age))

#output

# <class 'str'>
# <class 'int'>


age = "20"

age_number = int(age)

print(age_number)

# common conversion functions
str()
int()
float()
bool()
list()
tuple()
set()


#None

student_phone = None
if student_phone is None:
    print("Phone number not provided")

# PEP8 rules

# https://peps.python.org/pep-0008/


# frozenset

