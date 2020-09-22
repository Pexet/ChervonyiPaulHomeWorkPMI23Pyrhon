a = 1
#    провірка на те чи введене число А є в [1-109]
for a in range(1,109):
    while True:
        temp= input("Enter number(integer) in range [1-109] =")
        try:
            a = int(temp)
            break
        except ValueError:
            try:
                  float(temp)
                  print("Entered number is float type. PLEASE ENTER CORRECT DATAS")
            except ValueError:
                  print("VALUE ERROR PLEASE ENTER CORRECT DATAS")
    if a<=109 and a >=1:
        break

#    пошук числа для відповіді
n = 1
def finding_currentnum(a):
    n = 1
    while True:
        if ((n**n)%a)==0:
         break
        else:
            n+=1

    print(n)
    pass
n = 1
finding_currentnum(a)