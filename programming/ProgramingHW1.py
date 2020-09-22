import random

print("-------------------QUESTION #1--------------------")

#перевірка на правильність введення даних(чи користувач ввів потрібні для виконання програми умови)
while True:
      n = input("Enter mount of numbers(integer type) =")
      try:
            number_mounts = int(n)
            break
      except ValueError:
            try:
                  float(n)
                  print("Entered number is float type. PLEASE ENTER CORRECT DATAS")
            except ValueError:
                  print("VALUE ERROR PLEASE ENTER CORRECT DATAS")

print("Enter range of numbers")

while True:
      f_r = input("First number = ")
      try:
            first_number = int(f_r)
            break
      except ValueError:
            try:
                  float(f_r)
                  print("Entered number is float type. PLEASE ENTER CORRECT DATAS")
            except ValueError:
                  print("VALUE ERROR PLEASE ENTER CORRECT DATAS")

while True:
      s_r = input("Second number = ")
      try:
            second_number = int(s_r)
            break
      except ValueError:
            try:
                  float(s_r)
                  print("Entered number is float type. PLEASE ENTER CORRECT DATAS")
            except ValueError:
                  print("VALUE ERROR PLEASE ENTER CORRECT DATAS")


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
def GreateCommon(numbers):
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

i=1
GreateCommon(numbers)
print("-------------------QUESTION #2--------------------")