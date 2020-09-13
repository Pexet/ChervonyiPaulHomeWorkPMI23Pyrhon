import random

n = int(input("Enter mount of numbers ="))

print("Enter range of numbers")
first_number = int(input("First number = "))
second_number = int(input("Second number = "))

numbers = [0] * n

i=0
while i < n:
   numbers[i]= random.randint(first_number, second_number)
   i+=1
print("Our list =" , numbers)

i=1
while i < n:
    a1=a = int(numbers[i])
    b1=b = int(numbers[i-1])
    while a != 0 and b != 0:
      if a > b:
            a %= b
      else:
            b %= a

    gcd = a + b
    print("GCD(",a1,",",b1,") =",gcd)
    i+=1