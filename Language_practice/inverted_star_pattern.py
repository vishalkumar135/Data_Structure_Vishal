from cgi import print_arguments


n = int(input("enter the number of row"))
for i in range(n,0,-1):
    for j in range(0,n-i,+1):
        print(" ",end=" ")
    for j in range(0,i,1):
        print("*",end=" ")
    print('\n')
      