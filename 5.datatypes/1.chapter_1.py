# everything is object in python
sugar_amount = 2
print(f"Initial sugar: {sugar_amount}")

sugar_amount = 12
print(f"Second initial sugar: {sugar_amount}")


print(f"ID of 2: {id(2)}")
print(f"ID of 12: {id(12)}")


# never track the value based on value always track with identity
# numbers are not changeable but if you run python it is changed why
# python took this number new numbers it is 12 so it will point to 12 numbers not old one but old number is saved & so we are changing the reference only let's prove it

# Numbers are not changeable (it will create the reference everytime)