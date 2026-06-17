#basic example
# Shallow Copy

import copy


#Shallow Copy
original = ["Ali","Sara"] #normal list
copied = copy.copy(original)
copied.append("Usman")



# print(f"Original: {original}") #["Ali","Sara"]
# print(f"Copy: {copied}") #["Ali","Sara","Usman"]

#Problem When to use deep copy & shallow copy

original2 = [["Ali","Sara"],["Ahmed","Hina"]] #normal list
copied2 = copy.copy(original2)
copied2[0].append("Usman")



print(f"Original2: {original2}") 
print(f"Copy2: {copied2}") 

#Ouput
# Original2: [['Ali', 'Sara', 'Usman'], ['Ahmed', 'Hina']]
# Copy2: [['Ali', 'Sara', 'Usman'], ['Ahmed', 'Hina']]

#solution
# use
# copied2 = copy.deepcopy(original2)


#Deep Copy


original2 = [["Ali","Sara"],["Ahmed","Hina"]] #normal list
copied2 = copy.deepcopy(original2)
copied2[0].append("Usman")



print(f"Original2: {original2}") 
print(f"Copy2: {copied2}") 