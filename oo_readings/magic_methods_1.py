class Car:
    def __init__(self, name, year, color):
        self.name = name
        self.year = year
        self.color = color
        
    def __str__(self):
        return f'{self.color.title()} {self.year} {self.name} '
    
    def __repr__(self):
        color = repr(self.color)
        year = repr(self.year)
        name = repr(self.name)
        return f'Car({name}, {year}, {color})'
    
vwbuzz = Car('ID.Buzz', 2024, 'red')
print(vwbuzz)        # Red 2024 ID.Buzz
print(repr(vwbuzz))  # Car('ID.Buzz', 2024, 'red')