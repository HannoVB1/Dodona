# https://dodona.ugent.be/nl/courses/1523/series/16784/activities/1563511392
import math

def maximale_blootstelling(sound):
    if sound < 80:
        return -1.0

    repeat = True
    i = 80
    i2 = 0
    uur = 8
    while(repeat):
        i2 += 1
        if(sound >= i and sound < i +3 ):
            repeat = False
            return float(uur * 60 * 60)
        i += 3
        uur = uur /2
