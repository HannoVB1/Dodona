# https://dodona.ugent.be/nl/courses/1523/series/16782/activities/1186776322

def omgekeerd(dict):
    return {y: x for x, y in dict.items()}

def code39(zin,codeerssleutel):
    lijst = [*zin]
    sentence2 = ""
    for letter in lijst:
        sentence2 += codeerssleutel[letter.upper()] 
        sentence2 += "s"
    
    sentence2 = [*sentence2]
    sentence2.pop(len(sentence2)-1)
    return "".join(sentence2)

def decode39(zin,codeerssleutel):
    lijst = [*zin]
    word = ""
    sleutel = omgekeerd(codeerssleutel)
    cont = True
    amount = 0
    while amount <= len(lijst):
        letter = "".join([lijst[amount],lijst[amount+1],lijst[amount+2],lijst[amount+3],lijst[amount+4],lijst[amount+5],lijst[amount+6],lijst[amount+7],lijst[amount+8]])
        amount += 10
        word += sleutel[letter]
    return word
        
#decode39('SsSbSsBsBsBsSsSsSbBsBsSsBbSsSsSsSsBsSbBsBsSsSsSbBsSsSbBsSsBsBsSbSsBsSsSsSbSbSbSsSsSbSsBsBsSsBsSbBsSsSsSbSbSbSsSbBsSsSsBsSsBsSbBsSsSsBsSbBsSsSbSsBsSsBsSbSbSsSbS',{'L': 'BsSsBbSsS', 'I': 'BsSsSbSsB', 'B': 'SsBbSsSsB', '-': 'BbSsBsSsS', 'T': 'BsBsSsSbS', '3': 'BsSsSsBbS', 'R': 'SsSbBsSsB', 'K': 'BsSsBsSbS', '7': 'BsSsSbBsS', 'X': 'BsBbSsSsS', 'F': 'SsSsBsSbB', 'W': 'SsSsSsBbB', '1': 'SsBbSsBsS', '6': 'SsSsBsBbS', 'D': 'SbSsBsSsB', 'S': 'SsSbSsBsB', 'C': 'BbSsSsBsS', '5': 'SsSsBbSsB', 'V': 'BsSbSsSsB', 'N': 'SsBsSsSbB', '2': 'SsBbBsSsS', '.': 'SbSbSsSbS', '*': 'SsBsBbSsS', 'Q': 'SbBsSsBsS', '%': 'BbBsSsSsS', '9': 'SsBsBsSbS', 'U': 'BsSsSsSbB', 'Z': 'SsSbBsBsS', 'O': 'SsBsSbBsS', '/': 'BsBsSbSsS', '+': 'SbSsSbSbS', 'P': 'SbSsBsBsS', ' ': 'SsSbSbSbS', 'E': 'BbSsSsSsB', 'G': 'SbBsSsSsB', ',': 'BsSbSsBsS', 'H': 'SsSsBbBsS', 'M': 'SbSsSsBsB', '4': 'SsBsSbSsB', 'Y': 'SsBsSsBbS', '$': 'BsSbBsSsS', '0': 'SbSbSbSsS', 'J': 'SsSsSbBsB', 'A': 'SbBsBsSsS'})