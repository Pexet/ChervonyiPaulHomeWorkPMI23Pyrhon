import random

class Iterator:
    def __init__(self, n, a, b):
        self.i=0
        self.num = 0
        self.mount = n
        self.firs = a
        self.second = b

    def __iter__(self):
        return self

    def __next__(self):
        if self.i==self.mount:
            raise StopIteration
        self.i +=1
       
        self.num = random.randint(self.firs, self.second)
        return self.num