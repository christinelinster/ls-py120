class Foo():
    def __init__(self):
        type_name = self.__class__.__name__
        print(f'I am a {type_name} object')

foo = Foo()