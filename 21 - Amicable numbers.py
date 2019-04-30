import math

def divSum(n) : 
    result = 0
    for i in range(2,int((math.sqrt(n)))+1):
        if (n % i == 0): 
            if (i == (n/i)) : 
                result += i 
            else : 
                result += i + n//i 
          
    return (result + 1)

n=10000
tot=0
for i in range(n):
    if i == divSum (divSum (i)) and i != divSum(i):
        tot += i

print(tot)