# https://dodona.ugent.be/nl/courses/1523/series/16782/activities/431253538
def vertalingToevoegen(word1,word2,dictionary):
    dictionary[word1] = word2

def vertaling(word,dictionary):
    if word in dictionary:
        return dictionary[word]
    return "???"