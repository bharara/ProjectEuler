# - Problem 33
# - Digit Cancelling Fractions
# 
# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8,
#  which is correct, is obtained by cancelling the 9s.
# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

from fractions import Fraction

def isDigitCanceling(i, j):
    li = str(i)
    lj = str(j)
    for di in list(li):
        if di in lj:
            rj = lj.replace(di, "", 1)
            ri = li.replace(di, "", 1)
            if int("".join(ri)) / int("".join(rj)) ==  i/j:
                return True
    return False


pi = 1
pj = 1
for i in range(10, 100):
    for j in range(10, 100):
        if i!=j and i%10 and j%10 and isDigitCanceling(i, j) and i/j < 1:
            print (i, j)
            pi *= i
            pj *= j

print (pi, pj, Fraction(pi, pj))
