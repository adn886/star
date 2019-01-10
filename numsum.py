x=int(input(" Enter no "))
#p=int(input("enter no. length "))
i=0

k=0
q=0
while(x!=0):
   b=int(x%10)
   
   q=int(x/10)
   
   
   
   k=k+b
   x=q
print(" sum= {} ".format(k))