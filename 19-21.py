from functools import lru_cache

def moves(h):
    a, b = h
    return (a+1,b),(a*2,b),(a,b+1),(a,b*2)

@lru_cache(None)
def game(h):
    if sum(h) >= 77: return 'W'
    if any(game(x) == 'W' for x in moves(h)): return 'P1'
    if all(game(x) == 'P1' for x in moves(h)): return 'V1'
    if any(game(x) == 'V1' for x in moves(h)): return 'P2'
    if all(game(x) == 'P1' or game(x) == 'P2' for x in moves(h)): return 'V2'

for s in range(1,69+1):
    g = game((7,s))
    if g != None:
        print(s, g)