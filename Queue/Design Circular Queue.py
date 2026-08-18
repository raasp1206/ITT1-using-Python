class MyCircularQueue(object):

    def __init__(self, k):
        self.queue = [0] * k
        self.max_size = k
        self.head = 0  
        self.tail = 0  
        self.count = 0 

    def enQueue(self, value):
        if self.isFull():
            return False
        self.queue[self.tail] = value
        self.tail = (self.tail + 1) % self.max_size
        self.count += 1
        return True

    def deQueue(self):
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % self.max_size
        self.count -= 1
        return True

    def Front(self):
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def Rear(self):
        if self.isEmpty():
            return -1
        last_index = (self.tail - 1 + self.max_size) % self.max_size
        return self.queue[last_index]

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.max_size
