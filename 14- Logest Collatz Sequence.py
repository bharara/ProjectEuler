# - Problem 14
# - Longest Collatz Sequence
# 
# The following iterative sequence is defined for the set of positive integers:
# n -> n/2 (even)
# n -> 3n+1 (odd)
# 
# It can be seen that this sequence (starting at 13 and finishing at 1 contains 10 terms.
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# 
# Which starting number, under one million, produces the longest chain?

def collatz(i):
    return (3*i + 1) if i%2 else i//2

def chainCount(i):
    if i in cache: return cache[i]

    j = collatz(i)
    k = chainCount(j) + 1
    cache[i] = k
    return k


n = 1000000
cache = {
    2: 2
}

large = 0
ans = 0
for i in range (2, n):
    c = chainCount(i)
    if c > large:
        large = c
        ans = i

print(large, ans)
