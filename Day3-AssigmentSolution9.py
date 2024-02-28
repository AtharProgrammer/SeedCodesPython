# Input: Number of terms to generate from the user
n_terms = int(input("Enter the number of terms in the Fibonacci series: "))

# First two terms
n1, n2 = 0, 1
count = 0

# Check if the number of terms is valid
if n_terms <= 0:
    print("Please enter a positive integer.")
elif n_terms == 1:
    print("Fibonacci sequence upto 1 term:")
    print(n1)
else:
    print("Fibonacci sequence:")
    while count < n_terms:
        print(n1, end=' ')
        nth = n1 + n2
        # Update values
        n1 = n2
        n2 = nth
        count += 1
