# Palindrome
def palin(num):
    return str(num) == str(num)[::-1]        

a = 100
large = 0
while a < 1000:
    b = a
    while b < 1000:
        if a*b > large and palin(a*b):
            large = a*b
            break
        b += 1
    if a*b > large and palin(a*b):
        break
    a += 1
    
print(large)

