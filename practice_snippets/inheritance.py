class Beverage:
    def drink(self):
        return "Chug chug chug!"
    
class Water(Beverage):
    pass

class Juice(Beverage):

    def drink(self):
        return "Drinking juice..."

class Coffee(Beverage):
    def drink(self):
        print(super().drink())
        return "Drinking coffee.."
    

water = Water()
juice = Juice()
coffee = Coffee()

beverages = [water, juice, coffee]

for bev in beverages:
    print(bev.drink())

# This demonstrates polymorphism through inheritance because the different Beverage types (Water, Juice, Coffee)
# respond to the same method call "drink". They can have their own implementation but Water inherits the default
# behaviour from beverage. 

# This also demonstrates inheritance because all the subclasses can use the drink method without defining themselves. 
