class Bird:
    def __init__(self, species):
        self.species = species

class Sparrow(Bird):
    pass

sparrow = Sparrow("sparrow")
print(sparrow.species)