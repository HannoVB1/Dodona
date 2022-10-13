# https://dodona.ugent.be/nl/courses/1523/series/16785/activities/113082360


t = float(input())

def isGelijk(a,b,c,t):
    return (a + b + c) == (a * b * c) == t


a = float(1.00)
A = 1
B = 1
C = 1
while(not isGelijk(A,B,C,t)):
    b = a + float(0.01)
    c = b + float(0.01)
    while(a + b + c < t and a * b * c < t):
        b += float(0.01)
        c += float(0.01)
        print(f"{a}   {b}   {c}   {t}")
    
    a = a - float(0.01)
    A = a
    B = b
    C = c
        


                


