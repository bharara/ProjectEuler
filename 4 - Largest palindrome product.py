# Palindrome
def palin(num):
    return str(num) == str(num)[::-1]        

large = 0
n = 906609 + 1
for a in range(100, 1000):
    for b in range(a, 1000):
        if a*b > n:
            break
        if a*b > large and palin(a*b):
            large = a*b
            break

print (large)
