x = int(input(" Enter no "))
p=x
i = 0

k = 0
q = 0
while(x != 0):
    b = int(x % 10)

    q = int(x/10)

    k = k+pow(b, 3)
    print(k)
    x = q
if k == p:
    print(" no                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   u enterd is armstrong ")
else:
    print(" no is !not armstrong ")
