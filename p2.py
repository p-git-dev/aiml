import math

def alphabeta(d, i, mx, v, a, b, h):
    if d == h:
        return v[i]

    best = -math.inf if mx else math.inf

    for j in range(2):
        val = alphabeta(d+1, 2*i+j, not mx, v, a, b, h)

        if mx:
            best = max(best, val)
            a = max(a, best)
        else:
            best = min(best, val)
            b = min(b, best)

        if a >= b:
            break

    return best

v = list(map(int, input("Enter leaf values: ").split()))
h = int(math.log2(len(v)))
print("Evaluated Value:", alphabeta(0, 0, True, v, -math.inf, math.inf, h))
