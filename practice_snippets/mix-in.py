class WorkMixin:
    def work(self):
        print("I am working hard!")
    
class DeliveryDriver(WorkMixin):
    pass

class Student(WorkMixin):
    pass

class Scientist(WorkMixin):
   def work(self):
       print("I don't want to work anymore")


delivery = DeliveryDriver()
student = Student()
scientist = Scientist()

for person in [delivery, student, scientist]:
    person.work()


# Mixins enable polymorphism by providing a common interface method, 
# allowing unrelated classes to respond to the same method calls

# This is different from duck typing because with mixins, 
# the classes are inheriting the same implementation. 

# With duck typing, the classes just happen to have the same method name, 
# but with potentially different implementations