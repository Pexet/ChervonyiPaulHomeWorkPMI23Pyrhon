import random
from LinkedList import *
#--------------------------------------
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

def fillList(list):
    print("Mount of numbers in array =")
    n = getNumber()
    for i in range(n):
        print("list[",i,"]=",end=' ')
        num=getNumber()
        list.append(num)
    
    print("Our array =",arr)
   
def fillListRandom(list):
    print("Mount of numbers in array =")
    n = getNumber()
    print("Choose range of random creating\n The lowest number= ")
    loww = getNumber()
    print("The highest number= ")
    high=getNumber()
    if (loww > high):
      temp = loww
      loww=high
      high=temp

    for i in range(n):
        num = random.randint(loww, high)
        list.append(num)
    
    print("Our array =",arr)
#------------------------------------------

while True:
    print("Enter 1 or 2 or 3 \n1 - Fill by hand \n2 - Fill by random \n3 - Exit program")
    chos = getNumber()
    arr = LinkedList()
    if chos==1: 
        fillList(arr)
        print("Inpur K =")
        k= getNumber()
        arr=move(arr,k)
        print("Result = ",arr)
    elif chos==2:
        fillListRandom(arr)
        print("Inpur K =")
        k= getNumber()
        arr=move(arr,k)
        print("Result = ",arr)
    elif chos==3:
        break
    else:
        print("Something went wrong! Try again") 
