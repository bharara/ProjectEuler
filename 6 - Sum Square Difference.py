n = 100

s1 = n*(n+1)/2
s1 *= s1
s2 = n*(n+1)*(2*n+1)/6

print(int(abs(s1-s2)))
