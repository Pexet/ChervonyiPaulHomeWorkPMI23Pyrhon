a = 1
n = 1

#    провірка на те чи введене число А є в [1-109]
for a in range(1,109):
    a=int(input("Input A = "))
    if a<=109 and a >=1:
        break

#    пошук числа для відповіді
while True:
    if ((n**n)%a)==0:
        break
    else:
        n+=1

print(n)
#пробую робити зміни без прописування а в автоматиці