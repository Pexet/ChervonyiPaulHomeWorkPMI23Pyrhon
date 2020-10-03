def getNumber():
     while type:
         getTempNumber=input()
         try:
             getTempNumber=int(getTempNumber)
         except ValueError:
             print('"'+  getTempNumber + '"' + ' - is not a right number')
             print("Please enter number again! =")
         else:
             break
     return getTempNumber

def outMatrix(matr):
    for row in matr: #output matrix n*n
        print(' '.join([str(elem) for elem in row]))

print("Enter N for square matrix =")
n = getNumber()

a=[[0]*n for i in range(n)] #matrix n*n

#for row in a: #output matrix n*n
#    print(' '.join([str(elem) for elem in row]))
i=0
j=0
for i in range(n):
    for j in range(n):
        if ((i<=j) and (i+j<n)) or ((i>=j)and(i+j>=n-1)):
            a[i][j]=1
outMatrix(a)