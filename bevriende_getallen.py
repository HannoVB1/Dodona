# https://dodona.ugent.be/nl/courses/1523/series/16785/activities/1258720912

nr1,nr2 = int(input()),int(input())

def findDivisions(nr):
    array = []
    for dividor in range(1,round((nr/2)+1)):
        if(nr % dividor == 0):
            array.append(dividor)
    return array

def addDivisions(array):
    total = 0
    for item in array:
        total += item
    return total

arrayNR1 = findDivisions(nr1)
arrayNR2 = findDivisions(nr2)

if(addDivisions(arrayNR1) == nr2 and addDivisions(arrayNR2) == nr1):
    print(f"{nr1} en {nr2} zijn bevriende getallen")
else:
    print(f"{nr1} en {nr2} zijn geen bevriende getallen")