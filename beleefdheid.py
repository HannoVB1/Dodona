# https://dodona.ugent.be/nl/courses/1523/series/16785/activities/2134730675
import math

def isbeleefd(number):
    power = 0
    while(True == True):
        uitkomst = math.pow(2,power)
        power += 1
        if(uitkomst == number):
            return "onbeleefd"
        if(uitkomst > number):
            break
    
    

