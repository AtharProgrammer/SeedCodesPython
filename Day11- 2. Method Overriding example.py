class Animal:
    def sound(self):
        print("Some generic sound")

class Dog(Animal):
    def sound(self):
        print("Woof")

class Cat(Animal):
    def sound(self):
        print("Meow")

dog = Dog()
cat = Cat()

dog.sound()  # Output: Woof
cat.sound()  # Output: Meow
