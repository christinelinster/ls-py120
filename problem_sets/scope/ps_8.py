class Car: 
    manufacturer = "Jaguar"

    def __init__(self, manufacturer):
        self.manufacturer = manufacturer

    def show_manufacturer(self):
        print(f"{self.manufacturer=}")
        print(f"{Car.manufacturer=}")


car = Car("Toyota")
car.show_manufacturer()