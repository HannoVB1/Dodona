# https://dodona.ugent.be/nl/courses/1523/series/16784/activities/581452346

def bovensteboven(number):
    arr = [*str(number)]

    bovensteboven = True
    for i in range(0,len(arr)):
        side1 = arr[i]
        side2 = arr[len(arr)-i -1]

        if(not((side1 == "0" and side2 == "0") or (side1 == "8" and side2 == "8") or (side1 == "6" and side2 == "9") or (side1 == "9" and side2 == "6") or (side1 == "1" and side2 == "1"))):
            bovensteboven = False
    
    return bovensteboven

def volgende(number):
    firstTime = True 
    while(not (bovensteboven(number)) or firstTime):
        firstTime = False
        number += 1
    return number