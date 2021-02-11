from Generator import generator
from ClassIterator import Iterator

def getNumber():     # inputing and ckecking number method
     while type:
         getTempNumber=input()                      # inputing
         try:                                        # checking if all is right
             getTempNumber=int(getTempNumber)
         except ValueError:                          # checking if input is not a number
             print('"'+  getTempNumber + '"' + ' - is not a right number. TRY AGAIN!')
         else:                                       # if inputing is right so end method
             break
     return getTempNumber # returning our number

def greateCommon(numbers, moun):# method for finding Greatest Common Divisor
    i=1
    while i < moun:
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

while True:
    print('Input how to create array:\n1 - by iterator\n2 - by generator\n3 - exit')
    choise=getNumber()
    
    if choise==1 or choise==2:
        print('Input mount of numbers in array: ')
        moun=getNumber()
        print('Input range:')
        fir=getNumber()
        sec=getNumber()

        if (fir > sec):
            temp = fir
            fir=sec
            sec=temp

        finish = []
        if choise==1:
            print('\nBy iterator')
            iter_object=Iterator(moun, fir, sec)
            for q in iter_object:
               finish.append(q)
            print('Array= ', finish)
            greateCommon(finish, moun)
            
        elif choise==2:
            print('\n\nBy generator')
            for q in generator(fir,sec,moun):
               finish.append(q) 
            print('Array= ', finish)
            greateCommon(finish, moun)
        
    elif choise == 3:
        print('Program EXIT')
        break
    else:
        print('Something went wrong! Try again')