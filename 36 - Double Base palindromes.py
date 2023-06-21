# - Problem 36
# - Double-base Palindromes
# 
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

def binary(x):
    return int(bin(x)[2:])

def reverse (n):
    return n[::-1]

def isPalindromic(n):
    n = str(n)
    l = len(n)
    if l % 2:
        return n[:l//2] == reverse(n[l//2 + 1:])
    return n[:l//2] == reverse(n[l//2:])


n = 1000000
total = sum(i for i in range(1, n) if isPalindromic(i) and isPalindromic (binary(i)))
print(total)