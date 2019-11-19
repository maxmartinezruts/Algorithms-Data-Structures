"""
Author: Max Martinez Ruts
Date: October 2019
Description:

Creation of Range Tree data structure with search, insertion, deletion, rank implementations
"""


class RT:
    def __init__(self):
        self.root = None

    def check(self, n, p, side):
        print('checking', p.value)
        try:
            print('with child',  n.value)
        except:
            print('with none')
        if p != None:
            if side == 'left':
                if not (p.left == n and n.parent == p):
                    print(p, n, 'are not linked')
            if side == 'right':
                if not (p.right == n and n.parent == p):
                    print(p, n, 'are not linked')
            if n != None:
                self.check(n.left, n, 'left')
                self.check(n.right, n, 'right')



    """
    Description:
    Check for unbalances comparing left and right subtrees recursively by following a bottom-up path on the tree

    Complexity
    O(lg n) Since each iteration has O(1) and n of iterations is O(levels) = O(lg n)
    """

    def balance(self, root):
        x = root
        lh = self.get_k(root.left)
        rh = self.get_k(root.right)
        print('checking balance on', root.value, lh, rh)
        if abs(lh - rh) > 1:
            if lh > rh:

                llh = self.get_k(root.left.left)
                lrh = self.get_k(root.left.right)

                if llh >= lrh:
                    y = root.left
                    self.r_left_left(x, y)
                else:
                    z = root.left
                    y = root.left.right
                    self.r_left_right(x, y, z)
            else:

                rlh = self.get_k(root.right.left)
                rrh = self.get_k(root.right.right)
                if rlh > rrh:
                    z = root.right
                    y = root.right.left
                    self.r_right_left(x, y, z)
                else:
                    y = root.right
                    self.r_right_right(x, y)
        if root.parent == None:
            return
        else:
            self.balance(root.parent)

    def rank(self, root):
        count = 0
        v = root.value
        while root != None:

            if root.value <= v:
                if root.left != None:
                    count += root.left.s
                count +=1
            root = root.parent
        return  count -1


    # Helper to get k in case node does not exist
    def get_k(self, node):
        if node == None:
            return 0
        else:
            return node.k

    # Helper to get size in case node does not exist
    def get_s(self, node):
        if node == None:
            return 0
        else:
            return node.s

    """
    Description:
    Add child and update pointer of parents
    """

    def add_child(self, parent, child, side):

        if parent != None:
            print('Adding ', child.value, ' to ', parent.value)

            if side == 'left':
                parent.left = child
            else:
                parent.right = child
            child.parent = parent

            print('node', parent.value, 'has new child', child.value, 'on', side)

        self.update_augmentations(child)

    """
    Description:
    Update sizes following a bottom-up approach

    Complexity: O(lg n) 
    Since O(levels) = O(lg n)
    """

    def update_augmentations(self, root):
        # Iterative method, could also be recursive
        while root != None:
            root.s = 1 + self.get_s(root.left) + self.get_s(root.right)
            root.k = max(self.get_k(root.left), self.get_k(root.right)) + 1
            # Update root of tree
            if root.parent == None:
                self.root = root
                print('root is ', root.value)
            root = root.parent

    """
    Description:
    Insert a new node to the tree

    Complexity: O(lg n) 
    Since it first has to go down to a leaf O(lg n) and then balance the tree, also O(lg n). The search is done recursively by following a bottom-up approach
    """

    def insert(self, root, value):
        try:

            print('inserting ', value, 'to', root.value)
        except:
            print('inserting ', value, 'to', 'empty')
        # If tree is empty
        if root == None:
            child = self.Node(value)
            self.add_child(None, child, None)
            self.balance(child)
            return child

        # If root is leave
        elif root.left == None and root.right == None:
            child = self.Node(value)
            if value < root.value:
                self.add_child(root, child, 'left')
            else:
                self.add_child(root, child, 'right')
            self.balance(child)
            return child

        # If value is on left
        elif value < root.value:

            # If left child exists -> search on left child
            if root.left != None:
                self.insert(root.left, value)

            # Otherwise generate new left child
            else:
                child = self.Node(value)
                self.add_child(root, child, 'left')
                self.balance(child)
                return child

        # If value is on right
        else:
            print('go right')
            # If right child exists -> search on right child
            if root.right != None:
                self.insert(root.right, value)

            # Otherwise generate new right child
            else:
                child = self.Node(value)
                self.add_child(root, child, 'right')
                self.balance(child)
                return child

    """
    Description:
    Remove node given a value by searching the node containing the value, removing by updating pointers and finally balancing

    Complexity: O(lg n) 
    Since search is O(lg n), updating pointers is O(1) and balancing is O(lg n)
    """

    def remove(self, value):
        node = self.search(self.root, value)

        # Case 1: Node is leaf
        if node.left == None and node.right == None:
            print('case 1', node.value)
            if node.parent != None:
                if node.parent.left == node:
                    node.parent.left = None
                if node.parent.right == node:
                    node.parent.right = None
            self.update_augmentations(node.parent)
            self.balance(node.parent)

            del node

        # Case 2: Node has left child only
        elif node.left != None and node.right == None:
            if node.parent != None:
                if node.parent.left == node:
                    node.parent.left = node.left
                if node.parent.right == node:
                    node.parent.right = node.left
            node.left.parent = node.parent
            self.update_augmentations(node.left)
            self.balance(node.left)

            del node

        # Case 3: Node has right child only
        elif node.left == None and node.right != None:
            if node.parent != None:
                if node.parent.left == node:
                    node.parent.left = node.right
                if node.parent.right == node:
                    node.parent.right = node.right
            node.right.parent = node.parent
            self.update_augmentations(node.right)
            self.balance(node.right)

            del node

        # Case 4: Node has two children
        elif node.left != None and node.right != None:
            s = self.successor(node)
            sp = self.search(self.root, s.parent.value)
            p = node.parent
            y = node.right
            z = node.left
            print(sp.value, 'spppppppppp', y.value, z.value)

            if s != node.right:
                s.parent = p
                s.right = y
                s.left = z
                if p != None:
                    if p.right == node:
                        p.right = s
                    elif p.left == node:
                        p.left = s
                    else:
                        print('nooooooooooooooooooooooooo')
                z.parent = s
                y.parent = s
                sp.left = None
                print(sp.value, 'spppppppppp', z.value, y.value, s.value, s.left.value, s.right.value)
                print('more', z.parent.value, y.parent.value, s)
                print(rt.search(s,72).parent.value)
                print(rt.search(s,20).parent.value)
                print(rt.search(s,44).parent.value)
                print(rt.search(s,9).parent.value)
                print(rt.search(s,7).parent)
                print(rt.search(s,2).parent.value)







                self.update_augmentations(sp)
                self.balance(sp)
            else:
                s.parent = p
                s.left = z
                if p != None:
                    if p.right == node:
                        p.right = s
                    if p.left == node:
                        p.left = s
                z.parent = s
                self.update_augmentations(s)
                self.balance(s)



            # del node

        return

    """
    Description:
    Find successor of a node

    Complexity: O(lg n) 
    Since O(levels) = O(lg n)
    """

    def successor(self, node):

        node = node.right
        while node.left != None:
            node = node.left

        return node

    """
    Description:
    Search for a node given its value, return None if any node contains this value

    Complexity: O(lg n) 
    Since O(levels) = O(lg n)
    """

    def search(self, root, value):
        if root == None:
            return None

        if root.value == value:
            return root
        else:
            if value < root.value:
                return self.search(root.left, value)
            else:
                return self.search(root.right, value)

    def r_left_right(self, x, y, z):
        print('-----------------------------', 'left_right')

        """
                   R                     R
                   |                     |
                   x                     y
                  / \                  /  \
                 z   A     --->       z    x
                / \                 / \   / \
               D   y               D  C  B  A
                  / \
                 C   B

        Executed if A -> {k-1), D -> (k-1) and B or C-> (k-1)
        """

        R = x.parent
        A = x.right
        B = y.right
        C = y.left
        D = z.left

        x.right = A
        x.left = B
        z.right = C
        z.left = D

        y.right = x
        y.left = z

        x.parent = y
        z.parent = y
        y.parent = R

        if B != None:
            B.parent = x
        if C != None:
            C.parent = z


        if R != None:
            if R.left == x:
                R.left = y
            if R.right == x:
                R.right = y

        self.update_augmentations(x)
        self.update_augmentations(z)

        return

    def r_left_left(self, x, y):
        print('-----------------------------', 'left_left')
        """
                     R                     R
                     |                     |
                     x                     y
                    / \                   / \
                   y   A     --->        C   x
                  / \                       / \
                 B   C                     B   A

        Executed if A -> {k-1), B -> (k+1) and C -> (k or k+1)
        """

        A = x.right
        B = y.left
        C = y.right
        R = x.parent

        y.right = x
        x.left = B

        x.parent = y
        y.parent = R

        if A != None:
            A.parent = x
        if B != None:
            B.parent = x

        if R != None:
            if R.left == x:
                R.left = y
            if R.right == x:
                R.right = y
        self.update_augmentations(x)

        return

    def r_right_left(self, x, y, z):
        print('-----------------------------', 'right_left')

        """
                           R                     R
                           |                     |
                           x                     y
                          / \                  /  \
                         A   z     --->       x    z
                            / \             / \   / \
                           y   D           A  B  C  D
                          / \
                         B   C

        Executed if A -> {k-1), D -> (k-1) and B or C-> (k-1)
        """

        R = x.parent
        A = x.left
        B = y.left
        C = y.right
        D = z.right

        x.left = A
        x.right = B
        z.left = C
        z.right = D

        y.left = x
        y.right = z

        x.parent = y
        z.parent = y
        y.parent = R

        if B != None:
            B.parent = x
        if C!= None:
            C.parent = z

        if R != None:
            if R.left == x:
                R.left = y
            if R.right == x:
                R.right = y

        self.update_augmentations(x)
        self.update_augmentations(z)

        return

    def r_right_right(self, x, y):
        print('-----------------------------', 'right_right')
        """
                     R                     R
                     |                     |
                     x                     y
                    / \                   / \
                   A   y     --->        x   C
                      / \               / \
                     B   C             A   B

        Executed if A -> {k-1), C -> (k+1) and B -> (k or k+1)
        """

        A = x.left
        B = y.left
        C = y.right
        R = x.parent

        y.left = x
        x.right = B

        x.parent = y
        y.parent = R

        if A != None:
            A.parent = x
        if B != None:
            B.parent = x

        if R != None:
            if R.left == x:
                R.left = y
            if R.right == x:
                R.right = y

        self.update_augmentations(x)

        return

    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None
            self.parent = None
            self.k = 0
            self.s = 0

# Test cases

rt = RT()
n5 = rt.insert(rt.root, 5)

n6 = rt.insert(rt.root, 6)

n7 = rt.insert(rt.root, 7)

rt.insert(rt.root, 1)
rt.insert(rt.root, 9)
rt.insert(rt.root, 2)
rt.insert(rt.root, 20)
rt.insert(rt.root, 72)
rt.insert(rt.root, 3)
rt.insert(rt.root, 44)
rt.insert(rt.root, 4)

print(rt.search(rt.root, 5).value)

n72 = rt.search(rt.root,72)
print(rt.rank(n72))
print(rt.search(rt.root,44))
print(rt.rank(rt.search(rt.root,44)))
print(rt.rank(rt.search(rt.root,20)))
print(rt.rank(rt.search(rt.root,9)))
print(rt.rank(rt.search(rt.root,7)))
print(rt.rank(rt.search(rt.root,5)))
rt.remove(6)
rt.remove(4)

print(rt.rank(rt.search(rt.root,44)))
print(rt.rank(rt.search(rt.root,20)))
print(rt.rank(rt.search(rt.root,9)))
print(rt.rank(rt.search(rt.root,7)))
print(rt.rank(rt.search(rt.root,5)))

