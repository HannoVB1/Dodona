# https://dodona.ugent.be/nl/courses/1523/series/16785/activities/654951832


p = int(input())
k = int(input())

def noot_Output(number):
    match number:
        case 0: return "geen noten"
        case 1: return "1 noot"
        case _: return f"{number} noten" 

for i in range(1,p+2):
    voorAap = k % p

    notenPerPersoon = int((k - voorAap) / p)

    if(not(i == p+1)):
     print(f"{noot_Output(k)} = {noot_Output(notenPerPersoon)} voor piraat#{i} en {noot_Output(voorAap)} voor de aap")
    else:
     print(f"elke piraat krijgt {noot_Output(notenPerPersoon)} en {noot_Output(voorAap)} voor de aap")
    
    k = int(k - (notenPerPersoon + voorAap)) 
        
