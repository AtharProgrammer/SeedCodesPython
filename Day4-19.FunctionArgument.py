
'''
When we call the function if we are not passing any argument the
default value is assigned.
'''
def empdetails(eid=1, ename="Anu", esal=10000):
    print ("Emp id =", eid)
    print ("Emp name = ", ename)
    print ("Empsal=", esal)
    print("*********")



empdetails()
empdetails(222)
empdetails(333, "Durga")
empdetails(111, "Gagan", 10.5)

