while 1:
    n = int(input())
    rn = 0

    def rnum(n):
        l = len(str(n))

        for i in range(l):
            d = n%10
            nn = n - d
            nnn = nn/10
            n = nnn

            global rn
            rn = rn + d*10**(l-i)

        return(int(rn/10))

    print(rnum(n))
