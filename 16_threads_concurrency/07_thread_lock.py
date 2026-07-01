#race problem
import threading

counter = 0
lock = threading.Lock()   #we must need to use this lock outside of the function


def increment():
    global counter
    for _ in range(100000):
        with lock: # Manual lock for safe side
            counter += 1


# [value for item in data]

# threads = [threading.Thread(target=increment) for _ in range(10)]
threads = [threading.Thread(target=increment) for _ in range(10)]
# threads = [increment() for _ in range(10)]

[t.start() for t in threads]
[t.join() for t in threads]


print(f"Final Counter: {counter}")

# Output
# 100,000 * 10 = 1000,000
# Final Counter: 1000000