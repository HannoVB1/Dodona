# https://dodona.ugent.be/nl/courses/1523/series/16786/activities/1437422481
import math
a = float(input())
b = float(input())
c = float(input()) 

dominant = math.pow(b,2) - 4*a*c

if(dominant < 0):
    print("geen wortels")
elif(dominant == 0):
    print("een wortel")
    wortel = -(b/(2*a))
    print(wortel)
elif(dominant > 0):
    wortel1,wortel2 = (-b + math.sqrt(dominant))/ (2*a),(-b - math.sqrt(dominant))/ (2*a)
    print("twee wortels")
    if(wortel1 <= wortel2):
        print(wortel1)
        print(wortel2)
    else:
        print(wortel2)
        print(wortel1)

