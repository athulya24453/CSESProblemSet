s = input()

le = len(s)

ll = {}

for l in s:
    if l in ll:
        ll[l] += 1

    else:
        ll[l] = 1

ll_items = list(ll.items())

l = ['A' for _ in range(le)]

j = 1

for e in ll_items:
    for i in range(e[1]//2):
        l[j] = e[0]
        l[-j] = e[0]
        j += 1


for e in l:
    print(e, end="")