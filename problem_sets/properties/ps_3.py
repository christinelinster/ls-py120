class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width
    
    @property
    def height(self):
        return self._height
    

my_rect = Rectangle(5, 10)
print(my_rect.width)
print(my_rect.height)
my_rect.width = 20
print(my_rect.width)