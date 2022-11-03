# https://dodona.ugent.be/nl/courses/1523/series/16788/activities/854408577


def ggd(num1, num2):
    deling = max(num1,num2) % min(num1,num2)
    if(deling!=0):
        return ggd(min(num1,num2),deling)
    else:
        return num2