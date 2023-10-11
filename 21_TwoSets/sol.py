n = int(input())

sum = n*(n+1)/2

if sum % 2 == 1:
    print("NO")
else:
    print("YES")
    
    if n%4 == 0:
        print(n//2)
        for i in range(1,n//2, 2):
            print(i, end= " ")
        for i in range(n//2+2, n+1, 2):
            print(i, end = " ")
        print()
        print(n//2)
        for i in range(2, n//2+1, 2):
            print(i, end= " ")
        for i in range(n//2+1, n,2):
            print(i, end = " ")

    if (n+1) % 4 == 0:
        print(n//2+1)
        print("1 2", end= " ")
        for i in range(4, n+1, 4):
            print(i, end = " ")
            print(i+3, end = " ")

        print()
        print(n//2)
        print(3, end = " ")
        for i in range(4,n+1,4):
            print(i+1, end= " ")
            print(i+2, end= " ")


