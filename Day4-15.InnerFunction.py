#Inner function can access outer function variables

def outer():
    x=12
    print("Outer function")
    name1="Amit"
    print(x,name1)
    def inner():
        print("inner function")
        name2="Anu"
        print(name1)
        print(name2)
    
    inner() #inner function calling


outer() # outer function calling
