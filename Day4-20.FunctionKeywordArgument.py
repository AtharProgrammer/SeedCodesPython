'''
Keyword Arguments / Named Arguments

The keywords are mentioned during the function call along with
their corresponding values. These keywords are mapped with
the function arguments so the function can easily identify the
corresponding values even if the order is not maintained during
the function call.
Using the Keyword Argument, the argument passed in function
call is matched with function definition on the basis of the name
of the parameter.
'''

def empdetails(name, role):
    print(name, role)

empdetails(name = "Amit", role = "Manager") #function calling
empdetails(role = "developer" , name = "anu") #function calling
