# what is function in python ?

# A function is a block of code that perform a specific task.

# def greet():
#     print("Hello, world!")

#paramteres recieve

# def print_order(name,chai_type): #function() = parameter
#     print(f"Order for {name} : {chai_type} please !")

# print_order("Hitesh","Masala")# functioncall("asd","asd") argument
# print_order("Aman","Ginger")
# print_order("Jia","Tulsi")

#return in function

#scope


#Scopes & Name resolution

# Local - inside a function
# Global - Top level script


#Local Scope
# def serve_chai():
#     chai_type = "Masala" #local scope variable
#     print(f"Inside function {chai_type}")

# serve_chai() #output Inside function Masala


#Global Scope
chai_order = "Tulsi" #Global
# print(f"{chai_order}")

# Enclosing scope


def chai_counter():
    chai_order = "lemon" # Enclosing scope
    def print_order():
        chai_order = "Ginger"
        print("Inner:", chai_order)
    print_order()
    print("Outer: ", chai_order)


chai_counter()
print("Global :", chai_order)



def make_chai():
    return "Here is your masala chai"
   




#Nothing implicity return None
#One Value
#Multiple
#early from a function

#Nothing implicity return None
def idle_chaiwala():
    pass

print(idle_chaiwala()) #None

#One Value
make_chai_var = make_chai() #output "Here is your masala chai"

print(f"{make_chai_var}")

#Multiple

def chai_report():
    return 100,20,10

solid,remaining, _ =chai_report()
print(f"Solid: {solid}")
# print("Solid: " ,solid)

#Early return from a function
def chai_status(cup_left):
    if cup_left == 0:
        return "Sorry, chai over" #early from a function
    return "Chai is ready"


#Types of function

# 1. pure vs impure
# 2. recursive function
# 3. higher order function
# 4. anonymous/lambda function



#pure function
#A pure function always gives the same output for the same input and does not change anything outside itself.
def pure_chai(cups):
    return cups * 10


#impure function
# An impure function depends on or changes something outside the function.
total_chai = 0
def impure_chai(cups):
    global total_chai
    total_chai += cups


#Recursive Function
# A function that calls itself until a condition is met.

def countdown(number):
    if number == 0:
        print("Done")
        return
    print(number)
    countdown(number - 1)

countdown(3) #output 3,2,1,Done

#Higher-Order Function
# A function that takes another function as an argument or returns a function.

def greet():
    print("Hello")

#higher order function
def execute(func):
    func()

execute(greet)

#Anonymous / Lambda Function #(javascript arrow function)
#syntax lambda parameter: inner-logic
square = lambda x: x*x


square(5) #output 25


#full function
# def check(chai):
#     return chai != "kadak"
# vs
#short hand
lambda chai: chai != 'kadak'


#*args (in js you can say rest parameter)
# *args collects multiple positional arguments into a tuple.


def students(*args):
    print(args)

students("Ali", "Ahmed", "Sara") #output ('Ali', 'Ahmed', 'Sara')

# **kwargs
# **kwargs collects multiple keyword arguments into a dictionary.

def student_info(**kwargs):
    print(kwargs)

student_info(name="Ali", age=20, city="Karachi")

#output
# {
#     'name': 'Ali',
#     'age': 20,
#     'city': 'Karachi'
# }


#Loop Example
def student_info(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

student_info(name="Ali", age=20, city="Karachi")


#Builtin Function
# print()
# input()
# type()
# len() = length of items
# max()
# min()
# sum()
# enumerate()
# zip()
# any() (At least one true)
# all() (All True)

# https://docs.python.org/3/library/functions.html



#Document String
#dunderdoc = __ (double underscore)
# __doc__


#Doc String
def generate_bill(chai=0,samosa=0):
    """
    Calculate the total bill of samosa & chai
    :param chai: Number of chai cups (10 rupees each)
    :param samosa: NUmber of samosa (15 rupees each)
    :return: (total amount, thank you message as string)
    """
    total = chai*10 + samosa*15
    return total, "Thank you for visiting chaicode.com"




# ============================================
# map() → transform data
# multiply every number by 2

numbers = [1, 2, 3, 4]
# map(fun,variable)
doubled = list(map(lambda n: n * 2, numbers))

print(doubled)  # [2, 4, 6, 8]


# ============================================
# zip() → combine arrays
# combine names with marks

names = ["Ali", "Ahmed", "John"]
marks = [80, 90, 70]

result = list(zip(names, marks))

print(result)
# [('Ali', 80), ('Ahmed', 90), ('John', 70)]

# ============================================
# enumerate() → index + value together
# get index and item together

fruits = ["apple", "banana", "orange"]

for index, fruit in enumerate(fruits):
    print(index, fruit)

# 0 apple
# 1 banana
# 2 orange

# ============================================
# sorted() → returns new sorted list
# sort without changing original list

prices = [500, 200, 900, 100]

sorted_prices = sorted(prices)

print(sorted_prices)  # [100, 200, 500, 900]
print(prices)  

# ============================================
# any() → at least one True
# check if any user is admin

roles = ["user", "editor", "admin"]

is_admin_exist = any(role == "admin" for role in roles)

print(is_admin_exist)  # True

# ============================================
# all() → all must be True
# check if all users are active

statuses = [True, True, True]

all_active = all(statuses)

print(all_active)  # True

# ============================================
# isinstance() → type checking
# check variable type

price = 500

print(isinstance(price, int))   # True
print(isinstance(price, str))   # False


# ============================================
# sum() → total values
# total cart price

cart_prices = [100, 200, 300]

total = sum(cart_prices)

print(total)  # 600

# ============================================
# max() / min()
# highest and lowest marks

marks = [40, 90, 70, 100]

print(max(marks))  # 100
print(min(marks))  # 40

# ============================================
# len() → count items
# count list items

users = ["Ali", "Ahmed", "John"]

print(len(users))  # 3

# ============================================
# range() → generate numbers
# loop from 1 to 5

for number in range(1, 6):
    print(number)


# ============================================
# dict() → create object/dictionary
# create dictionary

user = dict(name="Ali", age=22)
print(user)

# {'name': 'Ali', 'age': 22}

# ============================================
# set() → remove duplicates
# remove duplicate values

numbers = [1, 2, 2, 3, 3, 4]
unique_numbers = set(numbers)
print(unique_numbers)

# {1, 2, 3, 4

# ============================================
# open() → file handling
# create and write file

with open("test.txt", "w") as file:
    file.write("Hello Python")
#with automatically closes the file.



# ============================================
# Most Important For Backend/AI Work

# Focus heavily on:

# map
# filter
# zip
# enumerate
# sorted
# any
# all
# sum
# isinstance
# open

# These are used everywhere in:

# Backend systems
# FastAPI
# AI agents
# Data processing
# Automation
# ML preprocessing



