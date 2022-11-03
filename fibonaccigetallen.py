# https://dodona.ugent.be/nl/courses/1523/series/16788/activities/546000908

def fib(nr):
    if nr == 0:
        return 0
    if nr == 1:
        return 1
    return fib(nr-1) + fib(nr-2)