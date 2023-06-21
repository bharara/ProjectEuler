# - Problem 34
# - Digit Cancelling Fractions
# 
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.

cache = {
    0: 1
}

def factorial (n):
    if n not in cache:
        cache[n] = n * factorial(n - 1)
    return cache[n]

def factorial_of_digits (n):
    return sum(factorial (int(i)) for i in list(str(n)))

n = 100000
total = sum(i for i in range(3, n) if factorial_of_digits (i) == i)
print(total)
