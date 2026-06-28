from multiprocessing import Process
import time


def crunch_number():
    print(f"Started the count process...")
    count = 0
    for _ in range(100_000_000):
        count += 1
    print(f"Ended the count process...")


if __name__ == "__main__":
    startTime = time.time()

    processOne = Process(target=crunch_number)
    processTwo = Process(target=crunch_number)


    # start

    processOne.start()
    processTwo.start()

    #join
    processOne.join()
    processTwo.join()

    endTime = time.time()

    print(f"Total time taken: {endTime - startTime:.2f} seconds")


#Output

# Started the count process...
# Started the count process...
# Ended the count process...
# Ended the count process...
# Total time taken: 1.15 seconds