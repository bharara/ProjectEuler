# - Problem 40
# - Champernowne's Constant
# 
# An irrational decimal fraction is created by concatenating the positive integers
# Find d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000

n = 100000

a = '0'
i = 1
while len(a) <= n:
    a += str(i)
    i += 1
     
def d(n):
    return int(a[n])
     
print (d(1)*d(10)*d(100)*d(1000)*d(10000)*d(100000)*d(1000000))
