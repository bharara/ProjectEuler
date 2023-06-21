# - Problem 38
# - Pandigital Multiples
# 
# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer

n = 9
s = "".join([str(x+1) for x in range(n)])

def isPandigital(n):
	return ''.join(sorted(n)) == s


def checkProduct(n):
	value = str(n)
	i = 2
	while len(value) < 9:
		value += str(n*i)
		i += 1
	return isPandigital(value)

mx = 98765//2 ## Largest 5 digit number possible divied by 2, 

value = 0
for i in range(mx, 0, -1):
	if checkProduct(i):
		value = i
		break
print (value, value*2)