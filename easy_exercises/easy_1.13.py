# Reverse Engineering

class Transform:
    def __init__(self, text):
        self.text = text

    def uppercase(self):
        return self.text.upper()
    
    @classmethod
    def lowercase(cls, string):
        return string.lower()


my_data = Transform('abc')
print(my_data.uppercase())              # ABC
print(Transform.lowercase('XYZ'))       # xyz