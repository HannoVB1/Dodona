# https://dodona.ugent.be/nl/courses/1523/series/16784/activities/1131866318


def waardering(price,exchangeRate):
    dollarBigMac = 4.07

    BigMacwisselkoers = price/dollarBigMac

    ratio = (BigMacwisselkoers - exchangeRate)/exchangeRate * 100

    if ratio <= -25:
        return "sterk ondergewaardeerd"
    elif ratio <= -5:
        return "ondergewaardeerd"
    elif ratio <= 5:
        return "ongeveer gelijk"
    elif ratio < 25:
        return "overgewaardeerd"
    elif ratio > 25:
        return "sterk overgewaardeerd"

def wisselkoersanalyse(priceString,number):
   arr = priceString.split()
   price = arr[0]
   arr.pop(0)
   arr = " ".join(arr)
   return f"De {arr} is {waardering(float(price),number)} ten opzichte van de dollar."