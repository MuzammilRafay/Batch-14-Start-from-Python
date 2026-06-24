#Example One
# def play_movie(movie):
#     if movie not in ["Avengers","Batman","Superman"]:
#         raise ValueError("Unsupported movie...")
#     print(f"Playing {movie}...")

# play_movie("Spider-Man")

#Example Two

class SeatNotAvailableError(Exception):
    pass

def book_ticket(available_seats,seats_requested):
    if available_seats == 0 or seats_requested == 0:
        raise SeatNotAvailableError("No seat available or invalid request")
    print("Ticket booked successfully")

book_ticket(0,2)