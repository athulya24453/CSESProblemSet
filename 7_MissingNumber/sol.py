n = int(input())
l = list(map(int,input().split()))

s = sum(l)
t = n*(n+1)//2

print(t-s)