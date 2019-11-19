"""
Author: Max Martinez Ruts
Date: October 2019
Description:

Creation of AVL data structure with search, insertion and deletion implementations
"""


class AVL:
    def __init__(self):
        self.root = None

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

    # Helper to get k in case node does not exist
    def get_k(self, node):
        if node == None:
            return 0
        else:
            return node.k

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

        self.update_ks_up(child)

    """
    Description:
    Update ks following a bottom-up approach

    Complexity: O(lg n) 
    Since O(levels) = O(lg n)
    """

    def update_ks_up(self, root):
        # Iterative method, could also be recursive
        while root != None:
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
            self.update_ks_up(node.parent)
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
            self.update_ks_up(node.left)
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
            self.update_ks_up(node.right)
            self.balance(node.right)

            del node

        # Case 4: Node has two children
        elif node.left != None and node.right != None:
            s = self.successor(node)
            print('successor', s.value)
            sp = self.search(self.root, s.parent.value)
            print(sp)
            if node.parent != None:
                if node.parent.left == node:
                    node.parent.left = s
                if node.parent.right == node:
                    node.parent.right = s
            s.parent = node.parent
            s.right = node.right
            s.left = node.left

            if sp != None:
                if sp.left == s:
                    sp.left = None
                if sp.right == s:
                    sp.right = None

            node.right.parent = s
            self.update_ks_up(sp)
            self.balance(sp)

            del node

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

        if R != None:
            if R.left == x:
                R.left = y
            if R.right == x:
                R.right = y

        self.update_ks_up(x)
        self.update_ks_up(z)

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
        if R != None:
            if R.left == x:
                R.left = y
            if R.right == x:
                R.right = y
        self.update_ks_up(x)

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
        if R != None:
            if R.left == x:
                R.left = y
            if R.right == x:
                R.right = y

        self.update_ks_up(x)
        self.update_ks_up(z)

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

        if R != None:
            if R.left == x:
                R.left = y
            if R.right == x:
                R.right = y

        self.update_ks_up(x)

        return

    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None
            self.parent = None
            self.k = 0


# Test cases

avl = AVL()
n5 = avl.insert(avl.root, 5)

n6 = avl.insert(avl.root, 6)

n7 = avl.insert(avl.root, 7)

avl.insert(avl.root, 1)
avl.insert(avl.root, 9)
avl.insert(avl.root, 2)
avl.insert(avl.root, 20)
avl.insert(avl.root, 72)
avl.insert(avl.root, 3)
avl.insert(avl.root, 44)
avl.insert(avl.root, 4)

print(avl.search(avl.root, 5).value)

avl.remove(6)
avl.remove(4)
print(avl.search(avl.root, 44))






