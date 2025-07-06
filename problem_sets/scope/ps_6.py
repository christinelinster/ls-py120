class Student:
    school_name = "Oxford"

    def __init__(self, name):
        self.name = name


student1 = Student("meimei")
student2 = Student("labubu")
print(student1.name, student1.__class__.school_name)
print(student2.name, student2.__class__.school_name)
