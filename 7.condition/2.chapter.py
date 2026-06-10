#Task

# Enter your preferred snack: cookies
# user said: cookies
# Great Choice! we'll serve you cookies

snack = input("Enter your preferred snack:").lower() #lowercase
print(f"user said: {snack}")

if snack == "cookies" or snack == "samosa":
    print(f"Great Choice! we'll serve you {snack}")
else:
    print("Sorry, we only serve cookies or samosa with tea")

