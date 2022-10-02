# https://dodona.ugent.be/nl/courses/1523/series/16786/activities/182880102

totaal = 0

for i in range(1,10):
    getal = int(input())
    totaal += getal * i
laatsteGetal = int(input())

if laatsteGetal == totaal % 11:
    print("OK")
else:
    print("FOUT")
