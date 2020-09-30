import random

print("-------------------QUESTION #1--------------------")

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

def greateCommon(numbers):# method for finding Greatest Common Divisor
    i=1
    while i < number_mounts:
        a1 = a = int(numbers[i])
        b1=b = int(numbers[i-1])
        while a != 0 and b != 0:
         if a > b:
            a %= b
         else:
            b %= a
        gcd = a + b
        print("GCD(",a1,",",b1,") =",gcd)
        i+=1

print("enter mount numbers = ")
number_mounts = getNumber()

print("Enter range of numbers")
print("Enter first num = ")
first_number = getNumber()
print("Enter second num = ")
second_number = getNumber()


numbers = [0] * number_mounts

if (first_number > second_number):
      temp = first_number
      first_number=second_number
      second_number=temp

i=0
while i < number_mounts:
   numbers[i]= random.randint(first_number, second_number)
   i+=1
print("Our list =" , numbers)


i=1
greateCommon(numbers)
