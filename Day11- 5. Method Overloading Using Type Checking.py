class MathOperations:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c

math = MathOperations()

print(math.add(2, 3))       # Output: Error: add() missing 1 required positional argument: 'c'
print(math.add(2, 3, 4))    # Output: 9
