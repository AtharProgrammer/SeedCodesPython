#The scope of the local variable only within the function, if we are
#calling outside of the function we will get error message.

def f():
    name = "amit"
    print (name)

f()
print (name)
# NameError: name 'n' is not defined
