n = 1000

import math

def s(a):
    m = math.floor((n-1)/a)
    r = (m * (a * (1 + m))) // 2
    return math.floor(r)


print(s(3) + s(5) - s(15))
