class Car:
    """Represents a car with its attributes and actions."""

    total = 0  # class variable

    def __init__(self, make, model, year, color, quantity=1, mileage=0):
        """Initializes the car's attributes."""
        Car.total += 1
        self.id = Car.total
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.quantity = quantity
        self.mileage = mileage

    def get_descriptive_name(self):
        """Returns a neatly formatted descriptive name of the car."""
        return f"{self.id} {self.year} {self.make} {self.model} ({self.color})"
    
    def get_info_with_quantity(self):
        """Returns a neatly formatted descriptive name of the car."""
        return f"{self.id} {self.year} {self.make} {self.model} ({self.color}) x{self.quantity}"

# Example usage:
#my_vehicle = Car("Honda", "Civic", 2023, "blue")
#print(my_vehicle.get_descriptive_name())  # Output: 2023 Honda Civic (Blue)
