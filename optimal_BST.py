import math

class Node:
    def __init__(self):
        self.left = None
        self.right = None


def O(K):
    print(K)
    if len(K)==1:
        for k in K:
            return K[k]
    if len(K)==0:
        return 0

    added_weight = 0
    for k in K:
        added_weight += K[k]


    min_guess = math.inf
    min_k = None


    for k in K:
        Kleft = {}
        Kright= {}
        for j in K:
            if j !=k:
                if j<k:
                    Kleft[j] = K[j]
                else:
                    Kright[j] = K[j]
        s = O(Kleft) + O(Kright)
        if  s < min_guess:
            min_k = k
            min_guess = s

    Kleft = {}
    Kright = {}
    for j in K:
        if j != min_k:
            if j < min_k:
                Kleft[j] = K[j]
            else:
                Kright[j] = K[j]
    return O(Kleft) + O(Kright) + added_weight





K = {1:1,2:10,3:8,4:9}

print(O(K))
