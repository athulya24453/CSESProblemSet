s = input()

c = 0
max = 0

for i in range(len(s)-1):

    if s[i+1] == s[i]:
        c += 1

    else: 
        if c > max:
            max = c

        c = 0

if c>max:
    max = c

print(max+1)

