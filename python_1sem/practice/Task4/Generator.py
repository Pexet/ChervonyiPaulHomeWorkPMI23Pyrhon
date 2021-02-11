import random

def generator(a,b,n):
    i=0
    while i<n:
        yield random.randint(a,b)
        i+=1