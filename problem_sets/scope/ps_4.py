class Dog:
    def __init__(self, breed):
        self._breed = breed

    def get_breed(self):
        return self._breed
    

goldy = Dog("Golden Retriever")
poods = Dog("Poodle")

print(goldy._breed)
print(poods.get_breed())
