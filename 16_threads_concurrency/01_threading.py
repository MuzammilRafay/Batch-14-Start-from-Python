import threading
import time


def take_order():
    for i in range(1,4):
        print(f"Brewing chai for #{i}")
        time.sleep(3)

def brew_chai():
    for i in range(1,4):
        print(f"Brewing chai for #{i}")
        time.sleep(3)

#Create Threads
order_thread = threading.Thread(target=take_order) #One thread responsible for take order
brew_thread = threading.Thread(target=brew_chai) #One thread responsible for brew chai

#we need to start the thread to work


#multi-thread example
order_thread.start()
brew_thread.start()

#wait for both to finish
order_thread.join()
brew_thread.join()



print(f"All orders taken & ordeer brewed")