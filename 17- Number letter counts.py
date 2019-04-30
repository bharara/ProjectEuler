unit = [3,3,5,4,4,3,5,5,4]
tunit = [3,6,6,8,8,7,7,9,8,8]
ten = [6,6,5,5,5,7,6,6]

# 1-9
t = sum(unit)

# 10-20
s = sum(tunit)
        
# 20-99
r = 0 
for n in ten:
    r += n*10 + t
    
# 1-99
h = t + r + s

# 100-999
n = t * 100 + h * 9 + 7 * 9 + 10 * 9 * 99

# Total
print(n + h + 11)
