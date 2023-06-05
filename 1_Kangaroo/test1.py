l1 = map(int(input().split()))

x1 = li[0]
x2 = l1[3]
v1 = l1[2]
v2 = l1[4]

t = 0

while t<=10000:
    s1 = x1+t*v1
    s2 = x2+t*v2

    if s1 == s2:
        print('Yes')
        break

    t+=1

else:
    print('No')
