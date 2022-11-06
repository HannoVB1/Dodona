# https://dodona.ugent.be/nl/courses/1523/series/16782/activities/531231333

def dubbel(list):
    for letter in list:
        if 2 <= list.count(letter):
            return letter
    return

def dubbel2(list):
    for letter in list:
        if 2 <= list.count(letter):
            return letter
    return False

def dubbels(lijst):
    nondubbel = set(lijst) 
    doubles = set()

    for i in range(0,len(lijst) - len(nondubbel)):
        if dubbel2(lijst) != False:
            doubles.add(dubbel2(lijst))
            item = dubbel2(lijst)
            for i in range(0,lijst.count(item)):
                lijst.pop(lijst.index(item))

    for item in doubles:
        nondubbel.discard(item)

    return (nondubbel,doubles)