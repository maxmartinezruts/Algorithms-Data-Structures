import math
def minimum_choice(C):
    print(C, 'minimize')
    if len(C) == 1:
        print(C[0])
        return -C[0]

    min_score = math.inf
    min_choice = None
    min_coin = None

    for c in [C[0],C[-1]]:

        Cguess = list(C)
        Cguess.remove(c)

        s = minimum_choice(Cguess)

        if min_score > s:
            min_score = s
            min_choice = Cguess
            min_coin = c

    return maximum_choice(min_choice) - min_coin
def maximum_choice(C):
    print(C, 'maximize')

    if len(C) == 1:
        return C[0]

    max_score = -math.inf
    max_choice = None
    max_coin = None

    for c in [C[0],C[-1]]   :

        Cguess = list(C)
        Cguess.remove(c)

        s = minimum_choice(Cguess)

        if max_score < s:
            max_score = s
            max_choice = Cguess
            max_coin = c

    return minimum_choice(max_choice) + max_coin

C = [4,42,39,19,25,6]

print(maximum_choice(C))