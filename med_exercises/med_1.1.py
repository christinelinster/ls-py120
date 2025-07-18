# Circular Buffer

class CircularBuffer:
    def __init__(self, size):
        self.buffer = [None] * size
        self.next = 0
        self.oldest = 0

    def get(self):
        value = self.buffer[self.oldest]
        if value != None: 
            self.buffer[self.oldest] = None
            self.oldest = (self.oldest + 1) % len(self.buffer)
        return value
    
    def put(self, obj):
        next_item = (self.next + 1) % len(self.buffer) # Next position
        if self.buffer[self.next] != None:
            self.oldest = next_item

        self.buffer[self.next] = obj
        self.next = next_item


buffer = CircularBuffer(3)

print(buffer.get() is None)          # True

buffer.put(1)
buffer.put(2)
print(buffer.get() == 1)             # True

buffer.put(3)
buffer.put(4)
print(buffer.get() == 2)             # True

buffer.put(5)
buffer.put(6)
buffer.put(7)
print(buffer.get() == 5)             # True
print(buffer.get() == 6)             # True
print(buffer.get() == 7)             # True
print(buffer.get() is None)          # True

buffer2 = CircularBuffer(4)

print(buffer2.get() is None)         # True

buffer2.put(1)
buffer2.put(2)
print(buffer2.get() == 1)            # True

buffer2.put(3)
buffer2.put(4)
print(buffer2.get() == 2)            # True

buffer2.put(5)
buffer2.put(6)
buffer2.put(7)
print(buffer2.get() == 4)            # True
print(buffer2.get() == 5)            # True
print(buffer2.get() == 6)            # True
print(buffer2.get() == 7)            # True
print(buffer2.get() is None)         # True