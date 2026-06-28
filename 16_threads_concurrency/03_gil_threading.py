import threading
import time



def brew_chai():
    print(f"{threading.current_thread().name} started brewing...")
    count = 0
    # it will take some time to execute 
    for _ in range(100_000_000):
        count += 1
    print(f"{threading.current_thread().name} finished brewing")



thread1 = threading.Thread(target=brew_chai,name="Barista-1")
thread2 = threading.Thread(target=brew_chai,name="Barista-2")

startTime = time.time() #start the time

thread1.start()
thread2.start()

#join mean wait for all things to complete
thread1.join()
thread2.join()

endTime = time.time() #end time

# .2f two decimal points 8.0000000 -> 8.00
print(f"Total time taken {endTime - startTime:.2f} seconds")

# Barista-1 started brewing...
# Barista-2 started brewing...
# Barista-1 finished brewing
# Barista-2 finished brewing
# Total time taken 2.20 seconds