# you are building a ticket into system for a railway app.
# based on seat type, show it is feature.

# Task:
# -input: "sleeper",'Ac',"general","luxury"
# -Match using match-case
# -Unkown -> show: "Invalid seat type"


user_input = input("Choose your seat types: (sleeper,Ac,General,luxary)").lower()

# swtich par hota tha javascript mein
match user_input:
    case "sleeper":
        print("Sleeper - No ac, beds available")
    case "ac":
        print("Ac - Air conditioned, comfort ride")
    case "general":
        print("General - Cheapest option, no reservation")
    case "luxury":
        print("Luxury - Premium seats with meals")
    case _:
        print("invalid seat type")
        