# - Problem 39
# - Integer Right Triangles
# 
# If p is the perimeter of a right angle triangle with integral length sides, {a, b, c}, there are exactly three solutions for p=120.
# For which value of p<=1000, is the number of solutions maximised?


def countOfSolution (x):
    count = 0
    for a in range (1, x//2):
        for b in range(a, x//2):
            c = (a*a + b*b) ** (0.5)
            if a + b + c == x:
                count += 1
                break
    return count

n = 1000

large = 0
maxAngle = 120
for i in range(12,n,12):
    j = countOfSolution (i)
    if j > large:
        large = j
        maxAngle = i

print(maxAngle)
