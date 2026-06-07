#  Loops
# Loops repeat code.

#For
students = ["Ali", "Sara", "Ahmed"]

for student in students:
    print(student)

#While
count = 1

while count <= 5:
    print(count)
    count += 1



for i in range(1, 5):
    print(i)


# enumerate()→ index + value
tickets = ["sleeper", "ac", "general"]
for index, ticket in enumerate(tickets):
    print(index, ticket)


#  zip() → combine multiple lists
names = ["Ali", "Ahmed"]
types = ["AC", "Sleeper"]

for name, t in zip(names, types):
    print(name, t)




#  Control Flow (break, continue, else)
# break → stop loop
# for i in range(5):
#     if i == 3:
#         break
#     print(i)
#  continue → skip iteration
# for i in range(5):
#     if i == 2:
#         continue
#     print(i)
#  else → runs if loop NOT broken
# for i in range(3):
#     print(i)
# else:
#     print("Loop finished")
