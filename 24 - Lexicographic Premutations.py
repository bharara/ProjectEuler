from itertools import permutations as per
l=list(per([0,1,2,3,4,5,6,7,8,9]))


n = 1000000
print("".join(str(x) for x in l[n-1]))