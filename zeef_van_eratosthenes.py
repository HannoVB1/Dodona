# https://dodona.ugent.be/nl/courses/1523/series/16783/activities/197813628

def zeef(number):
    arr = []
    
    prime = []
    stop = False
    for item in range(2,number+1):
        arr.append(item)
    length = len(arr)

    # m2>n    
    while(not stop):
        m = arr.pop(0)
        prime.append(m)
        if m*m > length:
            for item in arr:
                prime.append(item)
            stop = True
        else:
            for item in arr[arr.index(m*m):]:
                if item % m == 0:
                    arr.remove(item)
    return prime