n = int(input("Enter the number "))
flag = True
for div in range(2, n):
    if n % div == 0:
        flag = False

print("Prime" if flag == True else "Not Prime")
