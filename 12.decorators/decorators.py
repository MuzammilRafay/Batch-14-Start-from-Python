
# Wrapper
def wrapper(fun):
    def innerFunction():
        print("Starting...")
        fun()
        print("Ending...")
    return innerFunction;



@wrapper
def say_hello():
    print("hello")



say_hello()