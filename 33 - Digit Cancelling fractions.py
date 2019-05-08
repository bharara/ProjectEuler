n = 2

low = 10**(n-1)
high = low * 10

product = 1
for x in range(low, high):
    for y in range (low, x):
        
        ratio = int(x)/y
        x = str(x)
        y = str(y)
        
        if y[n-1] == '0' or x == y:
            continue
        
        flag = False
        for x0 in x:
            for y0 in y:
                if x0 == y0:
                    xi = x.index(x0)
                    yi = y.index(y0)

                    x_remain = x[:xi] + x[xi+1:]
                    y_remain = y[:yi] + y[yi+1:]

                    if int(y_remain) and ratio == int(x_remain) / int(y_remain):
                        flag = True
                        break
            if flag:
                break
        if flag:
            product *= ratio
            #print(ratio, x, y)

print(product)
