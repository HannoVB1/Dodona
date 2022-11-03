# https://dodona.ugent.be/nl/courses/1523/series/16783/activities/1333299580

def beweeg(tuple,direction):
    match direction:
        case ">": return (tuple[0] + 1, tuple[1])
        case "<": return (tuple[0] - 1, tuple[1])
        case "^": return (tuple[0], tuple[1] + 1)
        case "v": return (tuple[0], tuple[1] - 1)

def teruggekeerd(list):
    if list[0] == ">" and list[1] == "<":
        return True
    if list[0] == "<" and list[1] == ">":
        return True
    if list[0] == "v" and list[1] == "^":
        return True
    if list[0] == "^" and list[1] == "v":
        return True
    return False

def laatste_levende_positie(list):
    correct = 0
    coord = (0,0)
    for i in range(0,len(list)):
        if not i+1 == len(list):
            if not teruggekeerd([list[i],list[i+1]]):
                correct += 1
                coord = beweeg(coord,list[i])
            else:
                coord = beweeg(coord,list[i])
                break
        else:
            coord = beweeg(coord,list[i-1])
    return (correct +1,coord[0],coord[1])