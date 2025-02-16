
import matplotlib.pyplot as plt

# Scenario: Car dealership's inventory management system

# Task-1. You are tasked with creating a Python program to represent vehicles using a class. Each car should have attributes for maximum speed and mileage.
# Task-2. Update the class with the default color for all vehicles," white".
# Task-3. Additionally, you need to create methods in the Vehicle class to assign seating capacity to a vehicle.
# Task-4. Create a method to display all the properties of an object of the class. 
# Task-5. Additionally, you need to create two objects of the Vehicle class object that should have a max speed of 200kmph and mileage of 20kmpl with five seating capacities, and another car object should have a max speed of 180kmph and mileage of 25kmpl with four seating capacities.

class Vehicle:
    color = "white"
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
    
    def capacity(self, s_capacity):
        self.s_capacity = s_capacity

    def show_properties(self):
        print("Details of the Vehicle:")
        print("Color: ", self.color)
        print("Maximum Speed: ", self.max_speed)
        print("Mileage: ", self.mileage)
        print("Seating Capacity: ", self.s_capacity)

veh1 = Vehicle(200, 20)
veh1.capacity(5)
veh1.show_properties()
veh2 = Vehicle(180, 25)
veh2.capacity(4)
veh2.show_properties()
