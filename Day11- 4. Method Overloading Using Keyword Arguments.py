class MathOperations:
    def add(self, *args, **kwargs):
        if 'c' in kwargs:
            return sum(args) + kwargs['c']
        else:
            return sum(args)

math = MathOperations()

print(math.add(2, 3))           # Output: 5
print(math.add(2, 3, c=4))      # Output: 9
