# A tea stall offer differnt prices for different cup sizes.StopIteration
# write a program that calculates the price based on size

# Task
# -input: small,medium,large
# -small -> $10 medium, $15 large -> 20$
# if invalid show "Unknown cup size"

sizes_of_cup = input("choose your cup size (small,medium,large):").lower()
result = ""

if sizes_of_cup == "small":
    result = "Cup price is 10rs"
elif sizes_of_cup == "medium":
    result = "Cup price is 15rs"
elif sizes_of_cup == "large":
    result = "Cup price is 20rs"
else:
    result = "Unkown cup size"

print(result)


