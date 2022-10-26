# https://dodona.ugent.be/nl/courses/1523/series/16784/activities/522641350

def varkenswoord(str):
    klinkers = [*"aeiuo"]
    medeklinkers = [*"qwrtypsdfghjklzxcvbnm"]

    strArr = [*str]

    if firstLetter(str) == "klinker":
        for klinker in klinkers:
            if(strArr[0] == klinker):
                str = str + "way"
            if(strArr[0] == klinker.capitalize()):
                str = str + "way"
        return str
    else:

        eersteLetter = False
        hooftletter = False
        tweedeLetter = False
        for medeklinker in medeklinkers:
            if strArr[0] == medeklinker.upper():
                hooftletter = True
                eersteLetter = True
        
        for klinker in klinkers:
            if strArr[1] == klinker.upper():
                tweedeLetter = True
            
        while(firstLetter(strArr[0]) == "medeklinker" or (strArr[0].lower() == "u" and strArr[-1].lower() == "q")):
            if eersteLetter and hooftletter and tweedeLetter:
                letter = strArr.pop(0)
                strArr.append(letter)
                eersteLetter = False
            elif eersteLetter and hooftletter:
                letter = strArr.pop(0)
                strArr.append(letter.lower())
                eersteLetter = False
            else: 
                letter = strArr.pop(0)
                strArr.append(letter)
            
            
        
        strArr.append("a")
        strArr.append("y")
        if hooftletter:
            strArr[0] = strArr[0].upper()
        
        return "".join(strArr)

    
                    
def firstLetter(str):
    klinkers = [*"aeiuo"]
    medeklinkers = [*"qwrtypsdfghjklzxcvbnm"]

    for klinker in klinkers:
        if([*str][0].upper() == klinker.upper()):
            return "klinker"

    return "medeklinker"

def varkenslatijn(sentence):
    sentence = sentence.split(" ")
    for word in sentence:
        newWord = varkenswoord(word)
        sentence.pop(0)
        sentence.append(newWord)
    return " ".join(sentence)