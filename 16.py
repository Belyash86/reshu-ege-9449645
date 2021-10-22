def f(n):
    x = 0
    if n == 1: x = 1
    if n > 1: x = f(n-1)*(2*n + 1)
    return x

print(f(4))