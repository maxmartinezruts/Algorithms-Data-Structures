"""
Author: Max Martinez Ruts
Date: October 2019
Description:

Median consisting on Divide and Conquer algorithm that recursively finds the kth element on a list by
splitting the list in x list with smaller than m and a y list with larger values than m where m is chosen
using the median of medians method which has complexity O(n)

Proof
"""
import numpy as np


def median(V):
    if len(V) < 10:
        return np.median(np.array(V))
    v = len(V)

    if v % 2 == 0:
        return (select_kth(V, int(v / 2 - 1)) + select_kth(V, int(v / 2))) / 2
    else:
        return select_kth(V, int(v / 2))


"""
Description:

Select the kth element in an unsorted list by defining m = median of medians and then splitting V in x<m and y>m and
subsequently iterating in either x or y

Complexity: O(n)
Proof:

On each iteration, at least 3*(n/10 - 2) will be excluded, therefore only 7n/10 + 6 elements will be left
Recursion:
        Finding MoM        Recursion Select        Sorting V in MoM
T(n) =     T(n/5)     +      T(7n/10 + 6)      +          O(n)

T(n) = T(9n/10 + 6) + O(n) = T(0.9n + 6) + O(n)
T(n) = T(0.9^i*n + 6i) + i*O(n)                             Since 0.9^i converges to 0 fast with constant i we have
T(n) = T(6i + k) + iO(n) = O(n)
"""


def select_kth(V, k):
    m = median_of_medians(V)

    # Count elements smaller than m
    x = []
    y = []

    for v in V:
        if v < m:
            x.append(v)
        else:
            y.append(v)
    i = len(x)

    print(V, k, i, m, x, y)

    if len(x) == 0 or len(y) == 0:
        return sorted(V)[k]

    if i == k:
        return min(y)
    if i < k:
        return select_kth(y, k - i)
    if i > k:
        return select_kth(x, k)


"""
  |  |  |  |  |  |  
  |  |  |  |  |  |  |
  m1 m2 m3 m4 m5 m6 m7
  |  |  |  |  |  |  |
  |  |  |  |  |  |

Consists of splitting V into columns of length 5, sorting each column and getting its median and storing them in
m1 m2 m3 m4 m5 m6 m7... and then getting the median of [m1 m2 m3 m4 m5 m6 m7... m(n/5)]

Then if an M is selected using median of medians, at least 3*((n/10) - 2) items will be smaller than x and 
                                                  at least 3*((n/10) - 2) items will be larger than x

Leading to only 1 - 3(n/10 - 2) = 7n/10 + 6 items not being discarted
"""


def median_of_medians(V):
    k = 5

    M = []

    for i in range(0, len(V), k):
        c = sorted(V[i:i + k])
        if len(c) % 2 == 0:
            m = c[int(len(c) / 2) - 1]
        else:
            m = c[int(len(c) / 2)]
        M.append(m)

    # Recursively find median of M
    m = median(M)
    return m


V = [7, 3, 6, 3, 6, 8, 5, 2, 6, 2, 1]
