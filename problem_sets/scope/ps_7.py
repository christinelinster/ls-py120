class Student:
    _school_name = "Oxford"

    def __init__(self, name):
        self.name = name

    @classmethod
    def school_name(cls):
        return cls._school_name


print(Student._school_name)
print(Student.school_name())