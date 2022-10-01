# https://dodona.ugent.be/nl/courses/1523/series/16787/activities/567405275
from unicodedata import decimal


b,e,l = float(input()),float(input()),float(input())

kilometer = e - b
print(l / kilometer * 100)