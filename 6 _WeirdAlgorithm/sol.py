n = int(input())
l1 = [n]

while n!=1:
    if n%2 ==0:
        n = n//2

    else:
        n = 3*n+1

    l1.append(n)

print(" ".join(str(e) for e in l1))
