



class Collection:
    def __init__(self):
        self.arr = []

    def __str__(self):
        strng = ' '
        for i in range(len(self.arr)):
            strng += str(self.arr[i]) + '\n'
        return strng

    def add_to_arr(self, val):
        self.arr.append(val)
    
    def get_arr(self):
        return self.arr

    def read_from_file(self, file):
        with open(file) as of:
            while True:
                name = of.readline()
                salary = of.readline()

