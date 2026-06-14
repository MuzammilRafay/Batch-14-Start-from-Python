def serve_chai():
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"


chai = serve_chai()

print(next(chai))  # Cup 1
print(next(chai))  # Cup 2
print(next(chai))  # Cup 3


def infinite_chai():
    count = 1

    while True:
        yield f"Refill #{count}"
        count += 1



chai = infinite_chai()

print(next(chai))  # Refill #1
print(next(chai))  # Refill #2
print(next(chai))  # Refill #3
print(next(chai))  # Refill #4
print(next(chai))  # Refill #5
print(next(chai))  # Refill #6


