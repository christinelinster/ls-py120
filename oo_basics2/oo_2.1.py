# Generic Greeting

class Cat:
    @classmethod
    def generic_greeting(cls):
        print("Hello! I am a cat!")

kitty = Cat()       
kitty.generic_greeting() 
type(kitty).generic_greeting()