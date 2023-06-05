f = open("Sample.txt")
input = lambda : f.readline().strip() 



T = int(input())

def rnum(n):
    rn = 0
    l = len(str(n))

    for i in range(l):
        d = n%10
        nn = n - d
        nnn = nn/10
        n = nnn
        
        rn = rn + d*10**(l-i)

    return(int(rn/10))
    
def fact(n):
    l1 = []
    for i in range(n+1):
        if i != 0 and n%i == 0:
            l1.append(i)

    return(l1)
    
for t in range(T):
    add = 0
    n = int(input())
    l2 = fact(n)
    # print(l2)
    for e in l2:
        re = rnum(e)
        # print('e:'+str(e))
        # print('re'+str(re))
        if e == re:
            add += 1
        
            
    print('Case #'+str(t+1)+': '+str(add))
    
