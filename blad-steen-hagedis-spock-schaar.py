# https://dodona.ugent.be/nl/courses/1523/series/16786/activities/1647887074

speler1 = input()
speler2 = input()

array1 = ["schaar","blad","steen","Spock","hagedis"]
array2 = [["blad","hagedis"],["steen","Spock"],["hagedis","schaar"],["schaar","steen"],["Spock","blad"]]

if(not(speler1 == speler2)):
    for handgebaar in array1:
        if(handgebaar == speler1):
            speler1winners = array2[array1.index(handgebaar)]
        if(handgebaar == speler2):
            speler2winners = array2[array1.index(handgebaar)]
    # check wins
    for win in speler1winners:
        if(win == speler2):
            print("speler1 wint")
    for win in speler2winners:
        if(win == speler1):
            print("speler2 wint")
else:
    print("gelijkspel")

    





