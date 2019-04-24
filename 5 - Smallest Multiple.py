n = 20

from math import gcd

a = list(range(1,n+1))
lcm = a[0]

for i in a[1:]:
  lcm = int(lcm*i/gcd(lcm, i))

print (lcm)
