# - Problem 20
# - Factorial Digit Sum
# 
# Find the sum of the digits in the number 100!.

def factorial(n):
    if n == 2:
        return 2
    return n * factorial (n - 1)


n = 100
fact = list(str(factorial(n)))
s = sum(int(i) for i in fact)
print(s)
