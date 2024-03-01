#nonlocal keyword v/s global keyword

#Inside the function to represent the global value use global keyword.

def outer():
    name1="Amit"
    def inner():
        global name2
        name2 = "durga"

    inner() #inner function calling
    print("Outer Function – ", name1)
    print("Inner Function variable – ", name2)

outer()
