def DecimalToBinary(num):
     
    if num >= 1:
        DecimalToBinary(num // 2)
    print(num % 2, end = '')

def mulList(ls):
    m = 1

    for e in ls:
        m = m*e

    return m


n = int(input())

for _ in range(n):
    l2 = []
    l4 = []
    l = list(map(int,input().split()))

    b = DecimalToBinary(l[1])

    for i in str(b):
        l4.append(int(i))

    for e in range(len(l4)):
        l2.append(l[e]*2**(len(l4)-e)-1)

    for e in l2:
        l3 = [l[0]**e for e in l2]

    print(mulList(l3))
