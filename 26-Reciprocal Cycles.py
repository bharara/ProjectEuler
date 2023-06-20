# - Problem 26
# - Reciprocal Cycles
# 
# A unit fraction contains 1 in the numerator
#  Find the value of d < 1000 for which 1 / d contains the longest recurring cycle in its decimal fraction part.

def cycleLength(nem, dem):
    reminders = [1]

    while True:
        while dem > nem:
            nem *= 10

        rem = nem % dem
        if rem == 0:
            return 0
        
        if rem in reminders:
            return len(reminders) - reminders.index(rem)
        reminders.append(rem)
        nem = rem

n = 1000
largest = 0
answer = 1

for i in range(1, n):
    length = cycleLength(1, i)
    if length > largest:
        
        largest = length
        answer = i

print (answer, largest)