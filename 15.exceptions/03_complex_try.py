
# try:
# except:
# except:
# except:
# else:
# finally


def book_ticket(movie):
    try:
        print(f"Booking ticket for {movie}...")
        if movie == "unknown":
            raise ValueError("this movie is not available")
    except ValueError as e:
        print("Error:" , e)
    else:
        print(f"{movie} ticket booked successfully")
    finally:
        print("Next customer please")


# book_ticket("Avengers")
book_ticket("unknown")