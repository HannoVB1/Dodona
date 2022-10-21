# https://dodona.ugent.be/nl/courses/1523/series/16785/activities/1319193582
card = 1
totaal = 0
while(not card == 0):
    card = int(input())
    totaal += card
    if(totaal == 21):
        print("Gewonnen!")
        card = 0
    elif(totaal > 21):
        print(f"Verbrand ({totaal})")
        card = 0
    elif(card == 0):
        print(f"Voorzichtig gespeeld ({totaal})")