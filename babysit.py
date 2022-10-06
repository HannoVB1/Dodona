# https://dodona.ugent.be/nl/courses/1523/series/16786/activities/1797346540

hourStart,minuteStart,hourEnd,minuteEnd = int(input()),int(input()),int(input()),int(input())

start = float(hourStart + (minuteStart/60.0))
end = float(hourEnd + (minuteEnd/60.0))

if(not((end > start) and (start >= 18) and (end < 24 or end == 0))):
    print("ongeldige invoer")
else:
    if(end <= 21.5):
        totaal = (end-start) * 2
    elif(end > 21.5 and start >= 21.5):
        totaal = (end-start) * 4
    elif(end > 21.5 and start < 21.5):
        totaal = ((21.5 - start) *2) + ((end - 21.5) *4)

    print(totaal)