class Chai:
    temperature = "hot" #Attribute
    strength = "Strong" #Attribute

cutting = Chai()
print(cutting.temperature)

cutting.temperature = "Mild"
cutting.cup = "small"

print("After changing ",cutting.temperature)
print("cup size is  ",cutting.cup)
print("Direct look into the class ", Chai.temperature) 

# delete attribute

del cutting.temperature
del cutting.cup

print(cutting.temperature)
# print(cutting.cup) #qk by default value kuch nai hai or ye delete ho chuka hai to error dega is par