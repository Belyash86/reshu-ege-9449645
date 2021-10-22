def avtomat(n):
    n = str(bin(n)[2:])
    for _ in range(2):
        n = n + str(n.count('1')%2)
    return int(n,2)

for n in range(100):
    if avtomat(n) > 125:
        print(n, avtomat(n))
        break