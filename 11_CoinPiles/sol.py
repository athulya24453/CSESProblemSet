n = int(input())
for i in range(n):
    l = list(map(int,input().split()))

    if sum(l)%3!=0:
        print('NO')
        
    else:
        if max(l)-min(l)>max(l)/2:
            print('NO')

        else:
            print('YES')