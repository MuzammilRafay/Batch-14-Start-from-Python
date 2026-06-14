#What is comprehension
# List Comprehension
# Set Comprehension
# Dictionary Comprehension
# Generator Comprehension / Tuple Comprehension


# Comprehensions are a concise way to create lists,sets,dictionaries or generators in python using a single line of code
# It is a way to transform one iterable into another

# -----------------------------------------
# 1. LIST COMPREHENSION
# Make all names uppercase
# -----------------------------------------

#syntax
# [returnValue.upper() for singleValue in listValue]

names = ["Ali", "Ahmed", "Sara", "Ayan", "Ali"]

upper_names = [name.upper() for name in names]
print("List Comprehension:")
print(upper_names)

# Output:
# ['ALI', 'AHMED', 'SARA', 'AYAN', 'ALI']

# -----------------------------------------
# 2. SET COMPREHENSION
# Remove duplicate names
# -----------------------------------------

#syntax
# {returnValue for singleValue in listValue}
unique_names = {name for name in names}
print("\nSet Comprehension:")
print(unique_names)

# Output:
# {'Ali', 'Ahmed', 'Sara', 'Ayan'}

# -----------------------------------------
# 3. DICTIONARY COMPREHENSION
# Store name and its length
# -----------------------------------------

#syntax
# {key:value for singleValue in listValue}

names_with_lengths = {name: len(name) for name in names}

print("\nDictionary Comprehension:")
print(names_with_lengths)

# Output:
# {'Ali': 3, 'Ahmed': 5, 'Sara': 4, 'Ayan': 4}

# -----------------------------------------
# 4. GENERATOR COMPREHENSION
# Generate name lengths one by one
# -----------------------------------------

#syntax
# (returnValue for singleValue in listValue)


length_generator = (len(name) for name in names)

print("\nGenerator Comprehension:")
print(next(length_generator))
print(next(length_generator))
print(next(length_generator))
print(next(length_generator))
print(next(length_generator))



# =========================================
# SIMPLE FORMULAS
# =========================================

# LIST
# [value for item in data]

# SET
# {value for item in data}

# DICTIONARY
# {key:value for item in data}

# GENERATOR
# (value for item in data)

# =========================================
# EASY UNDERSTANDING
# =========================================

# []  -> List -> don't save in memory 
# {}  -> Set (unique)
# {k:v} -> Dictionary 
# ()  -> Generator (save in memory)

# General Syntax:
# [output for item in iterable if condition]