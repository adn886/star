i=1
j=1
n=int(input(" Enter no for column:- "))
m=int(input(" Enter no for row:- "))
p=n-1
q=n+1

for i in range(n):
    for j in range(m):
        
        if j>=q-i and j<=p+i:
            print("*",end="")
        else:
            print(" ",end="")
    print("\n")