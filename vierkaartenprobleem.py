# https://dodona.ugent.be/nl/courses/1523/series/16786/activities/1345385696

keuze = input()

if(keuze == "waarde"):
    getal = int(input())
    omdraaien = input()

    if(getal % 2 == 1 and omdraaien == "ja"):
        print(f"Fout: kaarten met waarde {getal} moeten niet gedraaid worden.")
    elif(getal % 2 == 1 and omdraaien == "nee"):
         print(f"Juist: kaarten met waarde {getal} moeten niet gedraaid worden.")
    elif(getal % 2 == 0 and omdraaien == "ja"):
        print(f"Juist: kaarten met waarde {getal} moeten gedraaid worden.")
    elif(getal % 2 == 0 and omdraaien == "nee"):
        print(f"Fout: kaarten met waarde {getal} moeten gedraaid worden.")
elif(keuze == "kleur"):
    kleur = input()
    omdraaien = input()
    if(kleur == "rood" and omdraaien == "ja"):
        print(f"Fout: kaarten met kleur {kleur} moeten niet gedraaid worden.")
    elif(kleur == "rood" and omdraaien == "nee"):
        print(f"Juist: kaarten met kleur {kleur} moeten niet gedraaid worden.")
    elif(omdraaien == "ja"):
        print(f"Juist: kaarten met kleur {kleur} moeten gedraaid worden.")
    elif(omdraaien == "nee"):
        print(f"Fout: kaarten met kleur {kleur} moeten gedraaid worden.")

else:
    print("error")
