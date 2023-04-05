# - Problem 3
# - Largest prime factor
# 
# The prime factors of 13195 are 5, 7, 13 and 29.
# 
# What is the largest prime factor of the number 600851475143 ?

def largest_prime_factor(n):
    # 2 if divisible by 2:
    answer = 0
    current = 2
    while n%current == 0:
        n //= current
        answer = current

    # Double increment going forward
    current = 3
    while current * current <= n:
        print (n, answer, current)
        if n%current == 0:
            n //= current
            answer = current
        else:
            current += 2

    if n > answer:
        answer = n
    
    return answer


n = 600851475143
print(largest_prime_factor(n))
