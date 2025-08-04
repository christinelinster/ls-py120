class Show:
    def start(self, people):
        for person in people:
            print(person.start_show())

class Singer:
    def start_show(self):
        return "I am singing"

class Dancers:
    def start_show(self):
        return "I am dancing"

class Cameramen:
    def start_show(self):
        return "I am filming"
    

people = [Singer(), Dancers(), Cameramen()]
show = Show()
show.start(people)

# This demonstrates duck typing because Singer, Dancers, and Cameramen are all unrelated classes that respond
# to the same start_show method. 

# The Show class doesn't care about the specific types, it just needs the objects to "quack like" people who start the show. 