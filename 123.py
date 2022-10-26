# https://dodona.ugent.be/nl/courses/1523/series/16784/activities/192047393

def evenOneven(getal):
    getallen = [*str(getal)]
    even = 0
    oneven = 0
    totaal = len(getallen)

    for getal in getallen:
        getal2 = int(getal)
        if(getal2 % 2 == 0):
            even += 1
        else:
            oneven += 1
    

    return (even, oneven)

    """
    >>> evenOneven(886328712442992)
    (10, 5)
    >>> evenOneven(10515)
    (1, 4)
    >>> evenOneven(145)
    (1, 2)
    """

def evenOneven2(getal):
    getallen = [*str(getal)]
    even = 0
    oneven = 0
    totaal = len(getallen)

    for getal in getallen:
        getal2 = int(getal)
        if(getal2 % 2 == 0):
            even += 1
        else:
            oneven += 1
    

    return f"{even} {oneven} {totaal}"

def volgende(getal):
    getal = evenOneven2(getal)
    nieuweGetal = ""
    arr = getal.split()
    
    if arr[0] != "0":
        nieuweGetal = f"{arr[0]}{arr[1]}{arr[2]}"
    else:
        nieuweGetal = f"{arr[1]}{arr[2]}"
    
    return int(nieuweGetal)


    """
    >>> volgende(886328712442992)
    10515
    >>> volgende(10515)
    145
    >>> volgende(145)
    123
    """

def stappen(getal):

    stappen = 0
    while(getal != 123):
        stappen += 1
        getal = volgende(getal)

    return stappen
    """
    >>> stappen(886328712442992)
    3
    >>> stappen(1217637626188463187643618416764317864)
    4
    >>> stappen(0)
    2
    >>> stappen(1)
    5
    >>> stappen(2)
    2
    >>> stappen(3)
    5
    """

if __name__ == '__main__':
    import doctest
    doctest.testmod()

stappen(886328712442992)