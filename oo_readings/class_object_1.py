class Car:

    def __init__(self, model, year, color):
        self._model = model
        self._year = year
        self.color = color
        self.speed = 0
        print(f'You have a {color} {year} {model}, nice!')

    def spray_paint(self, color):
        self.color = color
        print(f'Your {color} paint job looks great')

    @classmethod
    def mileage(cls, miles, gallon):
        print(f'{miles // gallon} miles per gallon')

    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, color):
        self._color = color

    @property
    def model(self):
        return self._model
    
    @property
    def year(self):
        return self._year

    @staticmethod
    def start_engine():
        print(f'The engine has started')

    def accelerate(self, kph):
        self.speed += kph
        print(f'You have accelerated {kph} per hour!')
    
    def brake(self, kph):
        self.speed -= kph
        print(f'You are slowing down {kph} per hour.')

    def turn_off_engine(self):
        self.speed = 0
        print(f'The engine has turned off.')
    
    def get_speed(self):
        print(f'Your current speed is {self.speed}.')


my_honda = Car('honda', 1999, 'blue')
my_honda.start_engine()
my_honda.accelerate(80)
my_honda.brake(20)
my_honda.get_speed()
my_honda.brake(20)
my_honda.turn_off_engine()
print(my_honda.color)
my_honda.color = 'green'
print(my_honda.color)
print(my_honda.year)
print(my_honda.model)
my_honda.spray_paint('yellow')
Car.mileage(351, 13)



    