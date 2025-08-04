class Ingredient:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return f"{self.quantity} {self.name}"
    
class Recipe:
    def __init__(self, name):
        self.name = name
        self.ingredients = []

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def get_shopping_list(self):
        return [str(ingredient) for ingredient in self.ingredients]


onion = Ingredient("onion", 2)
celery = Ingredient("celery", 5)

healthy_recipe = Recipe("vegan recipe")
healthy_recipe.add_ingredient(onion)
healthy_recipe.add_ingredient(celery)
shopping_list = healthy_recipe.get_shopping_list()
for item in shopping_list:
    print(item)

