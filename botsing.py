# https://dodona.ugent.be/nl/courses/1523/series/16786/activities/1301141031
x1,y1 = int(input()),int(input())
x2,y2 = int(input()),int(input())
x3,y3 = int(input()),int(input())
x4,y4 = int(input()),int(input())

botsingX = 0
botsingY = 0

if(x1 > x2):
    extraVar = x1
    x1 = x2
    x2 = extraVar

if(y1 > y2):
    extraVar = y1
    y1 = y2
    y2 = extraVar

if(x3 > x4):
    extraVar = x3
    x3 = x4
    x4 = extraVar

if(y3 > y4):
    extraVar = y3
    y3 = y4
    y4 = extraVar


i = x1 +1
while(i < x2):
    i2 = x3 +1
    while(i2 < x4):
        if(i == i2):
            botsingX = 1
            break
        i2 += 1
    i += 1

i = y1 +1
while(i < y2):
    i2 = y3 +1
    while(i2 < y4):
        if(i == i2):
            botsingY = 1
            break
        i2 += 1
    i += 1
    

if(botsingX == 1 and botsingY == 1):
    print("botsing")
else:
    print("geen botsing")
