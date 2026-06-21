colors = ["Red","Blue"]

#IndexError
try:
    print(colors[2])
except IndexError:
    print("The index you are trying to access does not exist")


# KeyError when key is missing in a dictionary
student_marks = {"Ali": 85, "Sara": 92}

try:
    print(student_marks["Ahmed"])  # KeyError
except KeyError:
    print("The student you are trying to access does not exist.")


# ZeroDivisionError when dividing by zero
try:
    result = 100 / 0  # ZeroDivisionError
except ZeroDivisionError:
    print("You cannot divide a number by zero.")

# TypeError when mixing different data types
try:
    print("Age: " + 25)  # TypeError
except TypeError:
    print("You cannot combine a string with an integer.")

# NameError when using an undefined variable
try:
    print(price)  # NameError
except NameError:
    print("The variable you are trying to use does not exist.")

# ValueError when converting an invalid value
try:
    age = int("twenty") #ValueError
except ValueError:
    print("Please enter a valid number.")




# try:
# except:
# except:
# except:
# else:
# finally

