# https://dodona.ugent.be/nl/courses/1523/series/16784/activities/1706631167

def csom(n):
    arr = [*str(n)]
    if(len(arr) != 1):
        total = 0
        for num in arr:
            total += int(num)
        return csom(total)
    return n