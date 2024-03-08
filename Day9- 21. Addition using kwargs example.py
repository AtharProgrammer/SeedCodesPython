def SumofValues(**kwargs):
    s=0
    for key,value in kwargs.items():
        print(key,value)
        s=s+value  
    print("Sum is =",s)
    
SumofValues(a=1,b=2,c=3)

