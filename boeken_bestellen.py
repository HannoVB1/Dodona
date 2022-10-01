# https://dodona.ugent.be/nl/courses/399/series/3960/activities/1886659767
BOEKPRIJS = 24.95
BOEKWINKELKORTING = 0.4
totaalprijs = 0

for i in range(1,61):
    if i == 1:
        totaalprijs += 3
    else:
        totaalprijs += 0.75
    totaalprijs += BOEKPRIJS * (1-BOEKWINKELKORTING)

print(totaalprijs)