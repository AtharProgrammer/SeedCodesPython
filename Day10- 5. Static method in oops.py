class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    @staticmethod
    def create_car(make, model):
        # Perform some validation or preprocessing if needed
        return Car(make, model)


# You can create a car using the static factory method
car = Car.create_car("Toyota", "Camry")
print(car.make, car.model)  # Output: Toyota Camry

