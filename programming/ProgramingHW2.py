def getNumber():     # inputing and ckecking number method
     while type:
         getTempNumber=input()                      # inputing
         try:                                        # checking if all is right
             getTempNumber=int(getTempNumber)
         except ValueError:                          # checking if input is not a number
             print('"'+  getTempNumber + '"' + ' - is not a right number')
         else:                                       # if inputing is right so end method
             break
     return getTempNumber # returning our number 

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
     
#test = [-2,5,6,-3,-4,3,-1]
#print(test)
#print(move(test,2))

print("Inpur K =")
k= getNumber()
print(move(arr,k))