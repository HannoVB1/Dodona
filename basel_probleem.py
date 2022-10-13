# https://dodona.ugent.be/nl/courses/1523/series/16785/activities/32506927

import math

#Regel 1
def euler(getal):
    uitkomst = 0
    for i in range(1,getal+1):
        uitkomst += float(1/(math.pow(i,2)))
    return uitkomst
print(round((euler(100)),11))

#Regel 2
def kleinsteWaarde():
    teller = 0
    getal = 1
    while(not (getal <= 1/100 and getal > 0)):
        teller += 1
        getal = abs(euler(teller) - ((math.pow(math.pi,2))/6))
    return teller
print(kleinsteWaarde())

