# https://dodona.ugent.be/nl/courses/1523/series/16785/activities/257342570


getal = int(input())
if getal <= 9 and getal > 0:
    ladder = ""
    for i in range(1,getal+1):
        ladder += str(i)
        print(ladder)