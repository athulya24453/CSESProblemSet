n = int(input())

for _ in range(n):
    rc_arr = list(map(int, input().split()))

    r = rc_arr[0]
    c = rc_arr[1]

    if c%2 == 1:
        print((c)**(2)-(r-1))

    elif r%2 == 0:
        print(r**(2)-(c-1))

    else:
        if c>r:
            print((c-1)**(2)+1-(r-1))

        else:
            print((r-1)**2+1-(c-1))