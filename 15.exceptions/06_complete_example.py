class InvalidMovieError(Exception):
    pass


def book_ticket(movie, seats):
    movies = {
        "Avengers": 500,
        "Batman": 400
    }

    try:
        if movie not in movies:
            raise InvalidMovieError("This movie is not available")

        if not isinstance(seats, int):
            raise TypeError("Number of seats must be an integer")

        total = movies[movie] * seats
        print(f"Booking confirmed for {seats} seat(s) of {movie}.")
        print(f"Total amount: Rs. {total}")

    except Exception as e:
        print("Error:", e)

    finally:
        print("Thank you for using our cinema service")


# Examples
# book_ticket("Avengers", 2)
# print()

# book_ticket("Spider-Man", 3)
# print()

# book_ticket("Batman", "two")

# Output
# Booking confirmed for 2 seat(s) of Avengers.
# Total amount: Rs. 1000
# Thank you for using our cinema service

# Error: This movie is not available
# Thank you for using our cinema service

# Error: Number of seats must be an integer
# Thank you for using our cinema service