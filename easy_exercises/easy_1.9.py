# Nobility

class WalkMixin:
    def walk(self):
        return f"{self} {self.gait()} forward"
    
class Animal:
    def __init__(self, name):
        self.name = name

    def __str__(self):
       return self.name

class Noble(WalkMixin):
    def __init__(self, name, title):
        self.name = name
        self.title = title

    def gait(self):
        return "struts"
    
    def __str__(self):
        return f"{self.title} {self.name}"

class Person(WalkMixin, Animal):
    def __init__(self, name):
        super().__init__(name)

    def gait(self):
        return "strolls"
    
    
class Cat(WalkMixin, Animal):
    def __init__(self, name):
        super().__init__(name)

    def gait(self):
        return "saunters"

class Cheetah(WalkMixin, Animal):
    def __init__(self, name):
        super().__init__(name)

    def gait(self):
        return "runs"

byron = Noble("Byron", "Lord")
print(byron.walk())  # "Lord Byron struts forward"
print(byron.name)    # "Byron"
print(byron.title)   # "Lord"