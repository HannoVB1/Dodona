# https://dodona.ugent.be/nl/courses/1523/series/16785/activities/1047652305
import math
from zipfile import LargeZipFile
# (rode rozen witte rozen)
RrWr = int(input())
WrBr = int(input())
operator = input()

if(RrWr >= WrBr):
    largest = RrWr
else:
    largest = WrBr

def bereken(operator,largest):
    W = 2
    found = False
    if(not found):
        for B in range(2,largest):
            for R in range(2,largest):
                if(operator == ">"):
                    if(B + R > W+B and R + W == RrWr and W+B == WrBr):
                        print(B)
                        print(W)
                        print(R)
                        found = True
                        break
                elif(operator == "<"):
                    if(B + R < W+B and R + W == RrWr and W+B == WrBr):
                        print(B)
                        print(W)
                        print(R)
                        found = True
                        break
    if(not found):
        B = 2
        for W in range(2,largest):
            for R in range(2,largest):
                if(operator == ">"):
                    if(B + R > W+B and R + W == RrWr and W+B == WrBr):
                        print(B)
                        print(W)
                        print(R)
                        found = True
                        break
                elif(operator == "<"):
                    if(B + R < W+B and R + W == RrWr and W+B == WrBr):
                        print(B)
                        print(W)
                        print(R)
                        found = True
                        break
    
    if(not found):
        R = 2 
        for W in range(2,largest):
            for B in range(2,largest):
                if(operator == ">"):
                    if(B + R > W+B and R + W == RrWr and W+B == WrBr):
                        print(B)
                        print(W)
                        print(R)
                        found = True
                        break
                elif(operator == "<"):
                    if(B + R < W+B and R + W == RrWr and W+B == WrBr):
                        print(B)
                        print(W)
                        print(R)
                        found = True
                        break

bereken(operator,largest)