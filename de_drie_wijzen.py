# https://dodona.ugent.be/nl/courses/1523/series/16785/activities/113082360
import math
import numpy as np

t = float(input())

def equals(a,b,c,t):
    return math.fsum([a,b,c]) == float(f"{a*b*c:.4f}") == float(f"{t:.4f}")

stop = False

for a in np.arange(0.01, 1.01, 0.01):
    for b in np.arange(a, t/2, 0.01):
        c = t - a - b
        a = round(a,2)
        b = round(b,2)
        c = round(c,2)
        # print(f"{a} {b} {c}")
        if equals(a,b,c,t):
            print(f"€{a:.2f} + €{b:.2f} + €{c:.2f} = €{a:.2f} x €{b:.2f} x €{c:.2f} = €{t:.2f}")
            stop = True
        if stop:
            break
    if stop:
        break
       

                


