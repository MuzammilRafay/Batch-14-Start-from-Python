# Membership Operator
# Used to check whether a value exists inside a list, string, tuple, dictionary, etc.


fruits = ["apple","banana","mango"]

print("apple" in fruits) #True
print("grape" not in fruits) #True


#Identity Operator
# Used to check whether two variables point to the same object in memory.

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b) # True
print(a is c) # False
print(a == c) # True


#Truthy False
#Some data that return always false

# False
# 0
# ""
# []
# {}
# None