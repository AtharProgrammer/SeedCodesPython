#Inner function : declaring function inside the another function

def outer():
    print("Outer function")
    def inner():
        print("inner function")
    def inner2():
        print("inner2")
     
    inner() # calling inner function
    inner2()
    
outer()# calling outer function
