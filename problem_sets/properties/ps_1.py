class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not name:
            raise ValueError("Name must not be empty")
        self._name = name


linda = Person('Linda')
print(linda.name)
linda.name = 'Meimei'
print(linda.name)
linda.name = ''
print(linda.name)