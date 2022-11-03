# https://dodona.ugent.be/nl/courses/1523/series/16788/activities/1092659960


def hanoi(nr):
    hanoi(nr-1)
    print(f"schijf ${nr}")