class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start_engine(self):
        print(f"The engine of {self.brand} {self.model} is starting.")

# Inheritance: Car inherits from Vehicle
class Car(Vehicle):
    def __init__(self, brand, model, num_doors):
        super().__init__(brand, model) # Call parent constructor
        self.num_doors = num_doors

    def honk(self):
        print("Beep beep!")

# Inheritance: Bike inherits from Vehicle
class Bike(Vehicle):
    def __init__(self, brand, model, type_of_bike):
        super().__init__(brand, model)
        self.type_of_bike = type_of_bike

    def kickstand(self):
        print(f"The {self.type_of_bike} bike kickstand is down.")

# Example usage
if __name__ == "__main__":
    my_car = Car("Toyota", "Corolla", 4)
    my_car.start_engine()
    my_car.honk()

    my_bike = Bike("Yamaha", "R15", "Sports")
    my_bike.start_engine()
    my_bike.kickstand()
