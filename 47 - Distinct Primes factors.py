def prfac(n):
    a=2
    c=1
    lst=[]
    while a*a<n:
        if n%a==0:
            n//=a
            if a not in lst:
                lst.append(a)
                c+=1
                continue
        else:
            a+=1
    return c


def check (i):

    for j in range (n):
        if prfac (i + j) != n:
            return False
    return True

# n=1
# while True:
#     if prfac(n)==4 and prfac(n+1)==4 and prfac(n+2)==4 and prfac(n+3)==4:
#         print(n,n+1,n+2,n+3)
#         break
#     n+=1

n = 4

i = 1
while True:
    if check (i):
        print(i)
        break
    i += 1