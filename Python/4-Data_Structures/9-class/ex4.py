class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"
    
class Bus(Vehicle):
        def seating_capacity(self, capacity):
             return super().seating_capacity(capacity)
    
bus = Bus("bus", 180, 12)
print(bus.seating_capacity())
