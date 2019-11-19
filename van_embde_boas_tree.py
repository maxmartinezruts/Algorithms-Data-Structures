"""
Author: Max Martinez Ruts
Date: October 2019
"""

import math

class VEB:
    def __init__(self, universe):
        self.u  = len(universe)
        self.universe = universe
        if 1 in universe:
            self.min = universe.index(1)
            self.max = self.u-universe[::-1].index(1)-1
        else:
            self.min = math.inf
            self.max = -math.inf
        self.cluster = []
        self.summary = []

        squ = math.sqrt(self.u)
        if squ%1 == 0 and squ != 1:
            squ = int(squ)
            print(squ)
            for g in range(int(squ)):
                galaxy = universe[g*squ:(g+1)*squ]
                cluster = VEB(galaxy)

                self.cluster.append(cluster)
                if 1 in galaxy:
                    self.summary.append(1)
                else:
                    self.summary.append(0)
            self.summary = VEB(self.summary)

            print(self.universe, self.min, self.max, self.summary.universe)

"""
SUCCESSSOR determines which is the next item given after an index x in a universe V

Claim: O(ln(ln(u)))
Proof:
- T(u) = T(u^(1/2)) + O(1)
- T(u) = T(u^(1/2^i)) + i
- Then write u as 2^(2^i), then u^(1/2^i) = 2 so if we say u = 2^(2^i), then i = lg(lg(u)) and expression becomes
- T(u) = T(2) + lg(lg(u)) = O(lg(lg(u)))
"""

def successor(V,x):

    i = high(x,V.u)

    # If index is smaller than smallest index, successor will be the smallest index
    if x<V.min and V.min != math.inf:
        return V.min
    if x>=V.max:
        return 'No Successor'

    # If len of u is 2 -> Predecessor will have index 1
    if V.u==2:
        j = 1

    # Look inside cluster
    elif low(x,V.u) < V.cluster[i].max:
        j = successor(V.cluster[i], low(x,V.u))

    # Look inside summary
    else:
        # Get high
        i = successor(V.summary, high(x,V.u))

        # Low will be the first item encountered in the cluster i
        j = V.cluster[i].min

    return index(i,j,V.u)

def insert(V,x):
    V.universe[x] = 1
    # If universe is empty
    if V.min == math.inf:
        V.min = x
        V.max = x

    # If index is smaller than smallest index
    if x<V.min:
        V.min = x

    if x>V.max:
        V.max = x

    if V.u>2:

        # If cluster is empty, insert x in summary
        # if V.cluster[high(x,V.u)].min == math.inf:
        insert(V.summary,high(x,V.u))

        # Repeat in higher order (cluster[i])
        insert(V.cluster[high(x,V.u)],low(x,V.u))


    else:
        V.max = max(x,V.max)
        V.min = min(x, V.min)

def delete(V,x):
    V.universe[x] = 0
    if 1 in V.universe:
        V.min = V.universe.index(1)
        V.max = V.u - V.universe[::-1].index(1) - 1
    else:
        V.min = math.inf
        V.max = -math.inf

    if V.u > 2:
        # Repeat in summary
        delete(V.summary, high(x, V.u))

        # Repeat in higher order (cluster[i])
        delete(V.cluster[high(x, V.u)], low(x, V.u))

#O(1)
def index(i,j,u):
    return int(i*math.sqrt(u)+j)

#O(1)
def high(x,u):
    return int(x/math.sqrt(u))

#O(1)
def low(x,u):
    return int(x%math.sqrt(u))

universe = [0,1,0,1,0,0,0,0,1,1,0,0,1,0,1,0]
# universe = []
V = VEB(universe)
for i in range(16):
    print(i, successor(V,i))

print('--------------------')

print('--------------------')
print(V.summary.cluster[0].min, V.summary.cluster[0].max, V.summary.cluster[0].universe)


insert(V,5)

print(V.summary.cluster[0].min, V.summary.cluster[0].max, V.summary.cluster[0].universe)

for i in range(16):
    print(i, successor(V,i))

print('--------------------')

print('--------------------')

delete(V,5)
print(V.summary.cluster[0].min, V.summary.cluster[0].max, V.summary.cluster[0].universe)

print(V.cluster[1].cluster[0].min)
print(V.cluster[1].cluster[0].max)

print(V.cluster[1].min)
print(V.cluster[1].max)
print(V.summary.min, V.summary.max)

print(V.cluster[1].summary.universe)
print(V.summary.universe)
print(V.min, V.max)
print(V.cluster[1].cluster[0].universe)
print(V.cluster[1].universe)
for i in range(16):
    print(i, successor(V,i))

print('--------------------')



