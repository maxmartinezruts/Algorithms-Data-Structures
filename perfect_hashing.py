import random

u = 400  # Universe
n = 100  # N entries
m = 100  # N slots

ht1 = {}

for k in range(m):
    ht1[k] = []


def h1(x):
    return x % m


def h2(x, l2):
    return x % (l2 ** 2)


rs = []

for i in range(n):
    rs.append(random.randint(0, u))

for r in rs:
    ht1[h1(r)].append(r)

for k in range(m):
    l = ht1[k]

    ht2 = {}
    l2 = len(l)

    for i in range(l2 ** 2):
        ht2[i] = []

    for

print(ht1)