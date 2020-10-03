def getNumber():
     while type:
         getTempNumber=input()
         try:
             getTempNumber=int(getTempNumber)
         except ValueError:
             print('"'+  getTempNumber + '"' + ' - is not a right number')
         else:
             break
     return getTempNumber

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

print("Mount of numbers in array =")
n = getNumber()
arr = [0]*n
i=0
while i<n:
    print("Number "+str(i+1)," = ")
    temp = getNumber()
    arr[i]=temp
    i+=1
print("Our array =",arr)

print("Inpur K =")
k= getNumber()
arr = move(arr,k)
print(arr)