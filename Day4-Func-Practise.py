#This is normal function example
def login():
    for x in range(10,20,2):
        print(x)

# This is argument example
def signup(username,password):
    if(username=="Ajit" and password=="12345"):
        print("Login Successful")
    else:
        print("You are not valid user")

# This is return value example
def checkevenodd(n):
    if(n%2==0):
        return 1
    else:
        return 0


def use():
    login()
    signup("Ajit","12345")
    checkevenodd(34)

use()

'''
x=checkevenodd(10)
if(x==1):
    print("Even")
else:
    print("Odd")

    
signup("Ajit","12345")
ch=int(input("Enter choice"))
if(ch==1):
    login()
else:
    print("Invalid choice")
'''
