def book_ticket(movie,numberOfTickets):
    try:
        numberOfTickets = int(numberOfTickets)
        price = {"Avengers":500,"Batman":400}[movie]
        # movies = {"Avengers":500,"Batman":400} -> movies["Avengers"] -> output 500
        total = price * numberOfTickets
        print(f"Total amount is {total}")
    except KeyError:
        print("Sorry, that movie is not available")
    except ValueError:
        print("Number of tickets must be a number")
    

# book_ticket("Batman",1)
# book_ticket("Spider-Man",1)
# book_ticket("Avengers",2)
# book_ticket("Avengers","two")

# int("two") -> ValueError: invalid literal for int() with base 10: 'two'




