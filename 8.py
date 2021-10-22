from itertools import product
k = 0
for p in product('ЛЕВИЙ', repeat = 5):
    for s in 'ЛЕВИЙ':
        if p.count(s) > 1: break
    else:
        if p[0] != 'Й' and 'ЕИ' not in ''.join(p):
            k += 1
print(k)