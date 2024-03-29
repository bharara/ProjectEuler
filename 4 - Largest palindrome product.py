# - Problem 4
# - Largest palindrome product
# 
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# 
# Find the largest palindrome made from the product of two 3-digit numbers.


def isPalidnrome(num):
    return str(num) == str(num)[::-1]

large = 0
for a in range(100, 1000):
    for b in range(a, 1000):
        if a*b > large and isPalidnrome(a*b):
            large = a*b
            break

print (large)
