import random

"""
DESCRIPTION:
Basic Quicksort consists of selecting the pivot as the first entry of the array, spliting the array in a left part with smaller
values and a right part with larger values and recursively quicksorting the resulting left and right parts such that

                            sorted = quicksorted(x) + pivot + quicksorted(y)        where x = left and y = right

O(n^2)

Proof: 
Worst case pivot is either the smallest or the largest, leading to unbalanced left and right sides. This leads to worst case:

        Recursion          Division 
T(n) =    T(n-1)       +      n
T(n) = T(n-i) + n*i

Substituting i by n
T(n) = T(n-n) + n^2 = O(n^2)
"""


def quicksort(V):
    if len(V) < 2:
        return V

    pivot = V[0]

    x = []
    y = []

    for i in V[1:]:
        if i < pivot:
            x.append(i)
        else:
            y.append(i)

    return quicksort(x) + [pivot] + quicksort(y)


"""
DESCRIPTION:
Variant of Basic Quicksort in which the pivot is repeatedly randomly chosen until a range of balance is achieved in order to ensure n lg(n) complexity

COMPLEXITY:

O(n lg(n))

Proof: 
If acceptable range of balance is chosen as 1/4<=4<=3/4, k being len(x)/len(v) where x is the left division of V:
    - Then P(balanced) = 1/2
    - Therefore E(balanced) = 2

And complexity becomes:

          Recursion        Division
T(n) = T(n/4) + T(3n/4) +    n*2*c

T(n) = T(n/16) + T(3n/16) + T(3n/16) + T(9n/16) + n*2*c*2
T(n) = T(n/64) + T(3n/64) + T(3n/64) + T(9n/64) + T(3n/64) + T(9n/64) + T(9n/64) + T(27n/64) + n*2*c*3

Looking at worst case:

T(n) = T(n*3^i/4^i) 2*c*n*i      Substituting i by lg_4/3(n) = i
T(n) = T(1) + 2*c*n*lg_4/3(n) = O(n lg(n))
"""


def paranoid_quicksort(V):
    if len(V) < 2:
        return V
    if len(V) == 2:
        return sorted(V)

    k = 0
    while not 1 / 4 <= k <= 3 / 4:
        r = random.randint(0, len(V) - 1)
        pivot = V[r]

        x = []
        y = []

        Vnew = list(V)

        Vnew.remove(V[r])

        for i in Vnew:
            if i < pivot:
                x.append(i)
            else:
                y.append(i)
        k = len(x) / (len(Vnew))

    return paranoid_quicksort(x) + [pivot] + paranoid_quicksort(y)


# Test CAses
V = [1, 4, 2, 5, 6, 3]
print(quicksort(V))
print(paranoid_quicksort(V))

