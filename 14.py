x = 2 * 216**6 + 3 * 36**9 - 432
k = 0
while x:
    if x % 6 == 5: k += 1
    x //= 6
print(k)