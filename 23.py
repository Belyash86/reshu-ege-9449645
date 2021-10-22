def f(start,end):
    if start == end: return True
    if start > end or start in (11,12): return False
    return f(start+1,end)+f(start+2,end)+f(start*3,end)

print(f(1,9)*f(9,30))