'''
AND (&): Performs bitwise AND on the operands. It returns 1 if both bits at the same position in both operands are 1, otherwise 0.

OR (|): Performs bitwise OR on the operands. It returns 1 if at least one of the bits at the same position in either operand is 1.

XOR (^): Performs bitwise XOR on the operands. It returns 1 if only one of the bits at the same position in the operands is 1, otherwise it returns 0 if both bits are 0 or both are 1.

NOT (~): Performs bitwise NOT on the operand. It flips the bits of the number, i.e., 1 becomes 0 and 0 becomes 1. Note that in Python, bitwise NOT is defined as ~x = -(x+1).

Left Shift (<<): Shifts the bits of the first operand left by the number of positions specified by the second operand. New bits on the right are filled with 0.

Right Shift (>>): Shifts the bits of the first operand right by the number of positions specified by the second operand. Whether new bits on the left are filled with 0 or 1 depends on the sign (positive or negative) of the original number in many environments,
though in Python, it's filled with 0 for positive numbers, making it an arithmetic shift.

'''

# AND
print(5 & 3)  # Output: 1 (0101 & 0011 = 0001)

# OR
print(5 | 3)  # Output: 7 (0101 | 0011 = 0111)

# XOR
print(5 ^ 3)  # Output: 6 (0101 ^ 0011 = 0110)

# NOT
print(~5)     # Output: -6 (~0101 = 1010, considering two's complement)

# Left Shift
print(5 << 1) # Output: 10 (0101 << 1 = 1010)

# Right Shift
print(5 >> 1) # Output: 2 (0101 >> 1 = 0010)
