'''
Variable Number of Arguments

This is very useful when we do not know the exact number of
arguments that will be passed to a function.
Or
we can have a design where any number of arguments can be
passed based on the requirement.
'''
def varlengthArgs(*x):
    for I in x:
        print(I)

varlengthArgs(1,2,3,4,5,6,7,8,9) #function calling
