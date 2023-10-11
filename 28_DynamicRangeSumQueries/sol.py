def sum(Tree,i): 
    sum = 0
    i = i+1 
    while i > 0: 

        sum += Tree[i]

        i -= i & (-i)
    return sum


def update(Tree ,n ,i ,v): 

    i += 1

    while i <= n: 

        Tree[i] += v 

        i += i & (-i) 
  


def construct(arr, n): 
    Tree = [0]*(n+1) 

    for i in range(n): 
        update(Tree, n, i, arr[i]) 

    return Tree 

if __name__ == "__main__":
    n, q  = map(int, input().split())
    arr = list(map(int, input(). split()))
    Tree = construct(arr, len(arr))

    for _ in range(q):
        o, a, b = map(int, input().split())

        if o == 1:
            update(Tree, len(arr), a-1, b - arr[a-1])

        if o == 2:
            ans = sum(Tree, b-1) - sum(Tree, a-2)
            print(ans)
