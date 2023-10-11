n = int(input())
a = n // 5

c = 0

while n>10:
    n = n//25
    c += n

ans = a+c


print(ans)