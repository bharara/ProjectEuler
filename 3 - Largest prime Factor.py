n = 600851475143

pr = 2
large = 0

while pr * pr <= n:
    if n%pr == 0:
        n //= pr
        large = pr
    else:
    	pr += 1

if n > large:
    large = n

print(large)
