# Pet Shelter

class Pet:
    def __init__(self, animal, name):
        self.animal = animal
        self.name = name

    def info(self):
        return f"a {self.animal} named {self.name}"

class Owner:
    def __init__(self, name):
        self.name = name
        self.pets = []

    def add_pet(self, pet):
        self.pets.append(pet)

    def number_of_pets(self):
        return len(self.pets)
    
    def print_pets(self):
        for pet in self.pets:
            print(pet.info())


class Shelter:
    def __init__(self):
        self.owners = {}
        self.unadopted_pets = []

    def add(self, pet):
        self.unadopted_pets.append(pet)

    def adopt(self, owner, pet):
        if pet in self.unadopted_pets:
            owner.add_pet(pet)
            self.unadopted_pets.remove(pet)
            if owner.name not in self.owners:
                self.owners[owner.name] = owner
        else:
            print("That pet is not available for adoption!")

    def print_unadopted_pets(self):
        print("The Animal Shelter has the following unadopted pets: ")
        for pet in self.unadopted_pets:
            print(pet.info())

    def print_adoptions(self):
        for name, owner in self.owners.items():
            print(f"{name} has adopted the following pets: ")
            owner.print_pets()
            print("")
            
shelter = Shelter()

cocoa   = Pet('cat', 'Cocoa')
cheddar = Pet('cat', 'Cheddar')
darwin  = Pet('bearded dragon', 'Darwin')
kennedy = Pet('dog', 'Kennedy')
sweetie = Pet('parakeet', 'Sweetie Pie')
molly   = Pet('dog', 'Molly')
chester = Pet('fish', 'Chester')
free = Pet('dog', 'Free')

shelter.add(cocoa)
shelter.add(cheddar)
shelter.add(darwin)
shelter.add(kennedy)
shelter.add(sweetie)
shelter.add(molly)
shelter.add(chester)

phanson = Owner('P Hanson')
bholmes = Owner('B Holmes')

shelter.adopt(phanson, cocoa)
shelter.adopt(phanson, cheddar)
shelter.adopt(phanson, darwin)
shelter.adopt(bholmes, kennedy)
shelter.adopt(bholmes, sweetie)
shelter.adopt(bholmes, molly)
shelter.adopt(bholmes, chester)
shelter.adopt(phanson, free)

shelter.print_unadopted_pets()
shelter.print_adoptions()
print(f"{phanson.name} has {phanson.number_of_pets()} "
      "adopted pets.")
print(f"{bholmes.name} has {bholmes.number_of_pets()} "
      "adopted pets.")

# P Hanson has adopted the following pets:
# a cat named Cocoa
# a cat named Cheddar
# a bearded dragon named Darwin

# B Holmes has adopted the following pets:
# a dog named Molly
# a parakeet named Sweetie Pie
# a dog named Kennedy
# a fish named Chester

# P Hanson has 3 adopted pets.
# B Holmes has 4 adopted pets.