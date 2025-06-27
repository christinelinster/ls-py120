class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return f'{self._first_name} {self._last_name}'.strip()
    
    @name.setter
    def name(self, name):
        parts = name.split()
        self._first_name = parts[0]
        self._last_name = ""

        if len(parts) > 1:
            self._last_name = parts[1]

    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name
    
    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name


bob = Person('Robert Smith')
rob = Person('Robert Smith')

print(bob.name == rob.name)