# https://dodona.ugent.be/nl/courses/1523/series/16784/activities/862295437

def codeer(t,s):
    s = [*codeLengte(len(t),s)]
    t = [*t]
    alphabet = [*"abcdefghijklmnopqrstuvwxyz".upper()]

    tekst = ""
    for i in range(0,len(t)):
        S = alphabet.index(s[i])
        try:
            O = alphabet.index(t[i])
        except:
            tekst += t[i]
        else:
            tekst += alphabet[((O + S) % 26)]
    
    return tekst

def decodeer(t,s):
    s = [*codeLengte(len(t),s)]
    alphabet = [*"abcdefghijklmnopqrstuvwxyz".upper()]

    tekst = ""
    for i in range(0,len(t)):
        S = alphabet.index(s[i])
        try:
            O = alphabet.index(t[i])
        except:
            tekst += t[i]
        else:
            tekst += alphabet[((O - S) % 26)]
    
    return tekst
            

    

def codeLengte(length,s):
    s = [*s]
    code = ""
    for i in range(1,length +1):
        code += s[(i % len(s)) -1]
    return code

print(codeer("DIT IS EXTREEM GEHEIM!","ZODIAK"))