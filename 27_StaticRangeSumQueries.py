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
  


def construct(arr, len): 
    Tree = [0]*(len+1) 

    for i in range(len): 
        update(Tree, len, i, arr[i]) 

    return Tree 

if __name__ == "__main__":
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))

    tree = construct(arr, len(arr))

    for _ in range(q):
        a, b = map(int, input().split())
        ans = sum(tree, (b-1)) - sum(tree, (a-2))
        print(ans)