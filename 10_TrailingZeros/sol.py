n = int(input())

t = 0

for i in range(len(str(n))):
    t+=n//5**(i+1)

print(t)