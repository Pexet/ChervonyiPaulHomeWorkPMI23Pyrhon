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

def createFillMatrix(n):
    matr=[[0]*n for i in range(n)]
    i=0
    j=0
    for i in range(n):
        for j in range(n):
           if ((i<=j) and (i+j<n)) or ((i>=j)and(i+j>=n-1)):
                matr[i][j]=1

    for row in matr: #output matrix n*n
        print(' '.join([str(elem) for elem in row]))            

while True:
    print("Enter 1 or 2 \n1 - Start program \n2 - Exit program")
    chos = getNumber()
    if chos==1:
        print("Enter N for square matrix =")
        n = getNumber()
        a = createFillMatrix(n)
    elif chos==2:
        break
    else:
        print("Something went wrong! Try again")