# Test 1
# You are preparing an order summary with customer names & their total bill.

# Task:
# use two lists one for names & one for bills.
# Print : "[Name] paid amount $[amount]"

# Hint
# use zip method


# Test 2

# explain this task in simple words
# you want to simulate tea heating.
# it starts at 40 C & boils at 100c
# Task:
# Use a while loop temperature by 15 until it reaches or exceeds 100
# print each temperature step



#Output:

#Temperature 40
#Temperature 55
#Temperature 70
#Temperature 85
#Temperature 100



# another example
users = [
    {"id":1, "total":100, "coupon":"P20"},
    {"id":2, "total":150, "coupon":"F10"},
    {"id":3, "total":80, "coupon":"P50"},
]

for user in users:
    print(user["coupon"])