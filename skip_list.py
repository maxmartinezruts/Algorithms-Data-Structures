"""
Author: Max Martinez Ruts
Date: October 2019
Description:

Skip List:

Data structure consisting in a group of double linked lists stacked above one other with the properties that
lists stacked in upper levels skip certain elements found in lower lists of lower levels.

Furthermore, if an element is found in list l, it will also be found in all other lists beneath l.

This data structure allows faster search than linked lists, since further elements in the lowest level list become
available by navigation thorough lists in upper levels.

An example of a Skip list would be:

l3 -> 5 ----------------- 9
      |                   |
l2 -> 5 ------- 7 ------- 9
      |         |         |
l1 -> 5 -- 6 -- 7 -- 8 -- 9

Where nodes can from different layers can be accessed using pointers that link nodes having same values in distinct layers

Using the given Skip list, search(8) would first go from l1 -> 5 to l2 -> 5 to l2 -> 7 to l1 -> 7 to l1 -> 8

Summary of complexity

Search: O(lg n)
"""
import random


class Node:
    def __init__(self, value, left, right, up, down):
        # Define neighbour pointers
        self.up = up
        self.left = left
        self.right = right
        self.down = down
        self.value = value

        # If down is empty, lv = 0, otherwise lv = down lode lv + 1
        self.lv = 0

        if self.down != None:
            self.lv = self.down.lv + 1

        layer[self.lv].append(self.value)


"""
Insert a node in the lowest lv by searching node s and inserting on the right on s on lv 0

Recursively inserting a node lv+1 with p = 1/2.

Complexity: O(lg n) w.h.p (with high probability)

Claim: only c lg n levels exist in skip list w.h.p where c is a constant
Proof: P(failure) = P(not <= c lg n levels)
                  = P(> c lg n levels)
                  = P(some element gets promoted greater than c lg n times)
                  <= n * P(element x gets promoted greater than c lg n times)
                  = n * (1/2)^(c lg n) = n/n^c =  1/n^(c-1) = 1/n^a with a = c - 1
Example: with n = 10 and c = 10
P(failure) = 1/10^9 = 0.000000001, meaning than only 0.000000001  times levels > c lg n
"""


def insert(value):
    # Create node to be inserted in lv 0
    n = Node(value, None, None, None, None)

    # Search the left neighbour of n
    s = search(pt, value, n.lv)

    # Temp variable
    r = s.right

    # Update pointers
    if s.right != None:
        s.right.left = n
    s.right = n
    n.left = s
    n.right = r

    # Repeating process one lv above with probability of 1/2
    rd = random.randint(0, 1)
    while rd == 1:
        rd = random.randint(0, 1)

        # Temp variable of node of previous lv
        temp = n

        # Create node to be inserted in new lv
        n = Node(value, None, None, None, n)

        # Up of previous n is new n
        temp.up = n

        # Search the left neighbour of n
        s = search(pt, value, n.lv)

        # Temp variable
        r = s.right

        # Update pointers
        if s.right != None:
            s.right.left = n
        s.right = n
        n.left = s
        n.right = r
    return


"""
Idea: 

Recursively search by accessing right nodes in the uppermost compatible node of the current note:
    1. Reach the uppermost node of the current examined node
    2. Try to go right. If right does not exist or overshoot, go down
        If down reached a lower level than admitted, solution was reached, since level is minimum and right would overshoot

Complexity: O(lg n)

Proof: Backward intuition

Staring with the found node, to reach 
"""


def search(root, value, lv):
    node = root
    print(root.value, root.lv)

    # Go to the uppermost node
    while node.up != None:
        node = node.up

    # Try to go right, if right does not exist or overshooting, go down and try again
    while node.right == None or node.right.value > value:
        if node.down != None and node.down.lv >= lv:
            node = node.down

        # If lowest lv encountered
        else:
            return node

    # Recursively search starting from new node
    return search(node.right, value, lv)


def delete():
    return


layer = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: []}

pt = Node(5, None, None, None, None)

for i in range(6, 100):
    print('----', i, '----')

    insert(i)

print('-------------------')

n = search(pt, 60, 0)
print(n.value, n.lv)

for l in layer:
    print(layer[l])