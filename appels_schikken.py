# https://dodona.ugent.be/nl/courses/1523/series/16787/activities/2071746302

appels = int(input())
rest = appels % 20
kisten = appels // 20
restAppelsInKisten = kisten % 35
palletten = kisten // 35

print(f"{palletten}\n{restAppelsInKisten}\n{rest}")

