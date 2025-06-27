# Exercise 1 How do we create a class and an object in Python?

'''
Write a program that defines a class and creates two objects from that class. 
The class should have at least one instance variable that gets initialized by the initializer.

What class you create doesn't matter, provided it satisfies the above requirements.
'''

class CoffeeShop:
    def __init__(self, name):
        self.name = name
    
    def serve(self):
        print(f'Welcome to our shop, {self.name}. We serve coffee!')


waves = CoffeeShop('waves')
starbucks = CoffeeShop('starbucks')

waves.serve()
starbucks.serve()

    