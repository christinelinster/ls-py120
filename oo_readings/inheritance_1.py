# Question 2 & 3

class Vehicles:
    num_of_vehicles = 0 
    def __init__(self):
        Vehicles.num_of_vehicles += 1
    
    @classmethod
    def vehicles(cls):
        return Vehicles.num_of_vehicles
    
class SignalMixin:
    def signal_left(self):
        print('Signalling left')

    def signal_right(right):
        print('Signalling right')
    
    def signal_off(self):
        print('Signal is now off')

class Car(SignalMixin, Vehicles):
    def __init__(self):
        super().__init__()

class Truck(SignalMixin,Vehicles):
    def __init__(self):
        super().__init__()

class Boat(Vehicles):
    def __init__(self):
        super().__init__()


print(Car.vehicles())     # 0
car1 = Car()
print(Car.vehicles())     # 1
car2 = Car()
car3 = Car()
car4 = Car()
print(Car.vehicles())     # 4
truck1 = Truck()
truck2 = Truck()
print(Truck.vehicles())   # 6
boat1 = Boat()
boat2 = Boat()
print(Boat.vehicles())    # 8

car1.signal_left()       # Signalling left
truck1.signal_right()    # Signalling right
car1.signal_off()        # Signal is now off
truck1.signal_off()      # Signal is now off
# boat1.signal_left()
# AttributeError: 'Boat' object has no attribute
# 'signal_left'

print(Car.mro())
print(Truck.mro())
print(Boat.mro())
print(Vehicles.mro())