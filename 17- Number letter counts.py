# - Problem 17
# - Number Letter Counts
# 
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

unit = [3,3,5,4,4,3,5,5,4]
tunit = [3,6,6,8,8,7,7,9,8,8]
ten = [6,6,5,5,5,7,6,6]

# 1-9
t = sum(unit)

# 10-20
s = sum(tunit)
        
# 20-99
r = sum(n*10 + t for n in ten) 
    
# 1-99
h = t + r + s

# 100-999
n = t * 100 + h * 9 + 7 * 9 + 10 * 9 * 99

# Total
print(n + h + 11)
