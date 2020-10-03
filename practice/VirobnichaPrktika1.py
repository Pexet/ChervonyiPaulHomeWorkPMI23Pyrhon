def finding_currentnum(a):
    n = 1
    while True:
        if ((n**n)%a)==0:
         break
        else:
            n+=1

    print(n)
    pass
#    провірка на те чи введене число А є в [1-109]
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

for a in range(1,109):
    print("Enter a number = ")
    a = getNumber()
    if a<=109 and a >=1:
        break
finding_currentnum(a)