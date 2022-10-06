# https://dodona.ugent.be/nl/courses/1523/series/16786/activities/408865752

munten123 = [1,2,3]
munten456 = [4,5,6]
munten789 = [7,8,9]

def balans(array1,array2,array3,richting):
    richtingen={
        "rechts":array1,
        "links":array2,
        "evenwicht":array3,
    }

    return richtingen.get(richting,"error")

richting1 = input()
# geeft de groep waar de valse munt in zit
munten = balans(munten123,munten456,munten789, richting1)

richting2 = input()
# geeft de juiste munt
valseMunt = balans(munten[0],munten[1],munten[2],richting2)

print(f"muntstuk #{valseMunt} is vervalst")