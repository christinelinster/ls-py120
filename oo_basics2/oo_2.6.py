# Colorful Cat

class Cat:
    COLOR = "purple"
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
    
    def greet(self):
        print(f"Hello! My name is {self.name} and I'm a {Cat.COLOR} cat!")

kitty = Cat('Sophie')
kitty.greet()
# Hello! My name is Sophie and I'm a purple cat!