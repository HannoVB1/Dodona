# https://dodona.ugent.be/nl/courses/1523/series/16787/activities/933531418
chirps = int(input())

tempF = 50 + ((chirps - 40)/4)
tempC = 10 + ((chirps - 40)/7)

print(f'temperatuur (Fahrenheit): {tempF}')
print(f'temperatuur (Celsius): {tempC}')