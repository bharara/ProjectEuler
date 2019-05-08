def isPan (i):

    for c in range(1, halfN):
        if int(i[:c]) * int(i[c:halfN]) ==  int(i[halfN:]):
            return int(i[halfN:])


import itertools

n = 9
if n%2:
    halfN = n//2 + 1
else:
    halfN = n//2

s = "".join([str(x+1) for x in range(n)])

p = list(itertools.permutations(s))
a = []

for i in p:
    x = isPan("".join(j for j in i))
    if x:
        #print(i, x)
        if x not in a:
            a.append(x)

#print(a)
print(sum(a))