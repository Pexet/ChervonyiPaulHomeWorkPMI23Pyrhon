while True:
        try:
            n = int(input("Mount of numbers in array = "))
            break
        except ValueError:
            print("ERROR PLEASE ENTER AN INTEGER")

arr = [0]*n
i=0
while i<n:
    while True:
        try:
            temp= int(input("Number "+str(i)+" = "))
            break
        except ValueError:
            print("ERROR PLEASE ENTER AN INTEGER")
    arr[i]=temp
    i+=1
print("Our array =",arr)

def move(numbers, k):
    result = []
    positive = [n for n in numbers if n >= 0]
    negative = [n for n in numbers if n < 0]
    positive = positive[::-1]
    for i in range(k):
        negative = [negative[-1]] + negative[:-1]
    pos = neg = 0
    for n in numbers:
        if n >= 0:
            result.append(positive[pos])
            pos += 1
        else:
            result.append(negative[neg])
            neg += 1
    return result
        
test = [-2,5,6,-3,-4,3,-1]
print(test)
print(move(test,2))

while True:
        try:
            k = int(input("K = "))
            break
        except ValueError:
            print("ERROR PLEASE ENTER AN INTEGER")

print(move(arr,k))