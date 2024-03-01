#nonlocal keyword v/s global keyword
#Inside the inner function to represent outer function variable use
#nonlocal keyword.

def outer():
    name1="Amit"
    print("Outer")
    def inner():
        print("Inner")
        nonlocal name1
        name1="durga"
        print(name1)
    inner()
    print("outer Function – ", name1)
    
outer()
