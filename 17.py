f = open('17.txt')
f = [int(f.readline()) for _ in range(10000)]
k = k_max = 0
for i in range(9999):
    for j in range(i+1, 10000):
        if (abs(f[i]-f[j]) % 45 == 0) and (f[i] % 18 == 0 or f[j] % 18 == 0):
            k += 1
            k_max = max(k_max, abs(f[i]-f[j]))
print(k,k_max)