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

def oneTimeSort(arr, index_arr):
    for i in range(0, len(arr)-1):
        for j in range(0, len(arr)-(i+1)):
            if arr[j]>arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1] , arr[j]
                index_arr[j], index_arr[j+1] = index_arr[j+1], index_arr[j]

def binary_search(arr, find):
    operations = 1
    lowwer = 0
    midle = len(arr) // 2
    upper = len(arr) - 1
    print("Search in [", lowwer, "," , upper, "]","Midle element =",arr[midle])
    while arr[midle] != find and lowwer <= upper:
        if find > arr[midle]:
            lowwer = midle + 1
        else:
            upper = midle - 1
        operations += 1
        midle = (lowwer + upper) // 2
        print("Search in[",lowwer,",",upper,"]","Midle element =",arr[midle])
    print("Mount of operations = ", operations)
    if lowwer > upper:
        return -1
    else:
        return midle

def sameElemetnOut(arr, arr_index, find):
    for i in range(0, len(arr)-1, 1):
        if arr[i]==find:
            print("index of our K =", arr_index[i])

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

print("---------------------------Question #2 (Binary)----------------------------------")
arr_index = []
for i in range(0, len(arr)):
    arr_index.append(i)

oneTimeSort(arr, arr_index)

print("Enter K which index will be showed = ")
K= getNumber()
mid = binary_search(arr, K)
sameElemetnOut(arr, arr_index, K)