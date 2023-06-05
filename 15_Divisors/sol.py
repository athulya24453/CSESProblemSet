n = int(input())
import math

l = []

for i in range(n):
    q = 0
    a = int(input()) 

    if math.sqrt(a)%1==0:
        for j in range(1,int(math.sqrt(a))+1):
            if a%j == 0:
                q += 2
        out = q-1

    else:
        for j in range(1,int(math.sqrt(a))+1):
            if a%j == 0:
                q += 2

                out = q

    l.append(out)

for i in range(len(l)):
    print(l[i])

    




