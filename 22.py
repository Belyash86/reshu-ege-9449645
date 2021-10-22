for i in range(10000000):
    x = i
    a=0; b=0
    while x > 0:
        if x%2 == 0:
            a += 1
        else:
            b += x%10
        x = x//10
    if a == 2 and b == 4:
        print(i)