# https://dodona.ugent.be/nl/courses/1523/series/16785/activities/364433585


h,b = int(input()),int(input())
direction = "rechtsboven"

x=1
y=1


def pocket(cordx, cordy):
    if(cordx == 0 and cordy == h):
        return "linkerbovenpocket"
    if(cordx == 0 and cordy == 0):
        return "linkeronderpocket"
    if(cordx == b and cordy == h):
        return "rechterbovenpocket"
    if(cordx == b and cordy == 0):
        return "rechteronderpocket"
    return False

def hit(cordx,cordy):
    if(cordx == b):
        return "rechterband"
    if(cordx == 0):
        return "linkerband"
    if(cordy == h):
        return "bovenband"
    if(cordy == 0):
        return "onderband"
    return False

def richting(richting,x,y,choice):
    match(richting):
        case "rechtsboven": 
            x += 1 
            y += 1
        case "rechtsonder":
            x += 1
            y -= 1
        case "linksboven":
            x -= 1
            y += 1
        case "linksonder":
            x -= 1
            y -= 1
    if choice == "x":
        return x
    else:
        return y

def changeRichting(richting,hit):
    nrichting = "error"

    if(richting == "rechtsboven" and hit == "bovenband"):
        nrichting = "rechtsonder"
    elif(richting == "rechtsonder" and hit == "onderband"):
         nrichting = "rechtsboven"
    elif(richting == "linksboven" and hit == "bovenband"):
         nrichting = "linksonder"
    elif(richting == "linksonder" and hit == "onderband"):
         nrichting = "linksboven"
    elif(richting == "rechtsboven" and hit == "rechterband"):
         nrichting = "linksboven"
    elif(richting == "linksboven" and hit == "linkerband"):
         nrichting = "rechtsboven"
    elif(richting == "rechtsonder" and hit == "rechterband"):
         nrichting = "linksonder"
    elif(richting == "linksonder" and hit == "linkerband"):
         nrichting = "rechtsonder"
    return nrichting 




while(not pocket(x,y)):
    x = richting(direction,x,y,"x")
    y = richting(direction,x,y,"y")

    if(pocket(x,y) != False):
        print(f"{pocket(x,y)} ({x}, {y})")
    elif(hit(x,y) != False):
        direction = changeRichting(direction,hit(x,y))
        print(f"{hit(x,y)} ({x}, {y})")
