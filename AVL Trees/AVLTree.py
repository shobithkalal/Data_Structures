import random as r


class Node:
    # DO NOT MODIFY THIS CLASS #
    __slots__ = 'value', 'parent', 'left', 'right', 'height'

    def __init__(self, value, parent=None, left=None, right=None):
        """
        Initialization of a node
        :param value: value stored at the node
        :param parent: the parent node
        :param left: the left child node
        :param right: the right child node
        """
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right
        self.height = 0

    def __eq__(self, other):
        """
        Determine if the two nodes are equal
        :param other: the node being compared to
        :return: true if the nodes are equal, false otherwise
        """
        if type(self) is not type(other):
            return False
        return self.value == other.value and self.height == other.height

    def __str__(self):
        """String representation of a node by its value"""
        return str(self.value)

    def __repr__(self):
        """String representation of a node by its value"""
        return str(self.value)

    def getHeight(self, node):
        return node.height


class AVLTree:

    def __init__(self):
        # DO NOT MODIFY THIS FUNCTION #
        """
        Initializes an empty Binary Search Tree
        """
        self.root = None
        self.size = 0

    def __eq__(self, other):
        # DO NOT MODIFY THIS FUNCTION #
        """
        Describe equality comparison for BSTs ('==')
        :param other: BST being compared to
        :return: True if equal, False if not equal
        """
        if self.size != other.size:
            return False
        if self.root != other.root:
            return False
        if self.root is None or other.root is None:
            return True  # Both must be None

        if self.root.left is not None and other.root.left is not None:
            r1 = self._compare(self.root.left, other.root.left)
        else:
            r1 = (self.root.left == other.root.left)
        if self.root.right is not None and other.root.right is not None:
            r2 = self._compare(self.root.right, other.root.right)
        else:
            r2 = (self.root.right == other.root.right)

        result = r1 and r2
        return result

    def _compare(self, t1, t2):
        # DO NOT MODIFY THIS FUNCTION #
        """
        Recursively compares two trees, used in __eq__.
        :param t1: root node of first tree
        :param t2: root node of second tree
        :return: True if equal, False if nott
        """
        if t1 is None or t2 is None:
            return t1 == t2
        if t1 != t2:
            return False
        result = self._compare(t1.left, t2.left) and self._compare(t1.right, t2.right)
        return result

    ### Implement/Modify the functions below ###

    def AVLTreeSetChild(self, parent, whichChild, child):
        """
        set child of parent node
        :param parent: parent node to set
        :param whichChild: location of child
        :param child: child to put
        :return: return true
        """
        if whichChild != "left" and whichChild != "right":
            return False
        if whichChild == "left":
            parent.left = child
            if child is not None:
                child.parent = parent
        if whichChild == "right":
            parent.right = child
            if child is not None:
                child.parent = parent
        AVLTreeUpdateHeight(parent)
        return True

    def AVLTreeReplaceChild(self, parent, currentChild, newChild):
        """
        replace child in AVLTree
        :param parent: parent
        :param currentChild: child to replace
        :param newChild: new child to put in
        :return: return false
        """
        if parent.left == currentChild:
            return self.AVLTreeSetChild(parent, "left", newChild)
        elif parent.right == currentChild:
            return self.AVLTreeSetChild(parent, "right", newChild)
        return False

    def AVLTreeGetBalance(self, root):
        """
        get the balance of the tree
        :param root: node to find balance of
        :return: returns balance
        """
        leftHeight = -1
        rightHeight = -1
        if root.left is not None:
            leftHeight = root.left.height
        if root.right is not None:
            rightHeight = root.right.height
        height1 = leftHeight - rightHeight
        return height1

    # for this helper function is better to use ==-2 or <-1?
    def AVLTreeRebalance(self, node):
        """
        rebalances the tree and does proper rotations
        :param node: node to rebalance
        :return: returns the balanced node
        """
        AVLTreeUpdateHeight(node)
        if self.AVLTreeGetBalance(node) < -1:
            if self.AVLTreeGetBalance(node.right) == 1:
                self.right_rotate(node.right)
            return self.left_rotate(node)
        elif self.AVLTreeGetBalance(node) > 1:
            if self.AVLTreeGetBalance(node) == -1:
                self.left_rotate(node.left)
            return self.right_rotate(node)
        AVLTreeUpdateHeight(node)
        return node

    def insert(self, node, value):
        """
        values to insert into a avl tree
        :param node: avl tree to be inserted in
        :param value: value inserted
        :return: none
        """
        valueNode = Node(value)

        if node is None:
            self.root = valueNode
            valueNode.parent = None
            self.size += 1
            return

        currentNode = node
        if currentNode is not None:
            if currentNode.value > value:
                if currentNode.left is None:
                    currentNode.left = valueNode
                    valueNode.parent = currentNode
                    self.size += 1
                else:
                    self.insert(node.left, value)
            elif currentNode.value < value:
                if currentNode.right is None:
                    currentNode.right = valueNode
                    valueNode.parent = currentNode
                    self.size += 1
                else:
                    self.insert(node.right, value)
            elif currentNode.value == value:
                return
            while currentNode is not None:
                AVLTreeUpdateHeight(currentNode)
                currentNode = currentNode.parent
            AVLTreeUpdateHeight(valueNode)
        node = node.parent
        if node is not None:
            self.AVLTreeRebalance(node)
            if node.parent is not None:
                self.AVLTreeRebalance(node.parent)

    def remove(self, node, value):
        """
        removes node if the value is present in avl tree
        :param node: avl tree
        :param value: value to delete in avl tree
        :return: node of subtree
        """

        if node is None:
            return None
        else:
            if node.value > value:
                self.remove(node.left , value)
            elif node.value < value:
                self.remove(node.right , value)
            elif node.value == value:
                if node.parent is not None:
                    if node.left is None and node.right is not None:
                        self.AVLTreeReplaceChild(node.parent , node , node.right)
                        parent = node.parent
                        while parent is not None:
                            AVLTreeUpdateHeight(parent)
                            parent = parent.parent
                        AVLTreeUpdateHeight(node.right)
                        self.size -= 1
                    elif node.right is None and node.left is not None:
                        self.AVLTreeReplaceChild(node.parent, node, node.left)
                        parent = node.parent
                        while parent is not None:
                            AVLTreeUpdateHeight(parent)
                            parent = parent.parent
                        AVLTreeUpdateHeight(node.left)
                        self.size -= 1
                    elif node.right is not None and node.left is not None:
                        max = self.max(node.left)
                        if max.value == node.left.value:
                            max.right = node.right
                            node.right.parent = max
                            self.AVLTreeReplaceChild(node.parent, node, max)
                            parent = node.parent
                            while parent is not None:
                                AVLTreeUpdateHeight(parent)
                                parent = parent.parent
                            AVLTreeUpdateHeight(max)
                            self.size -= 1
                        else:
                            self.size -= 1
                            self.AVLTreeReplaceChild(max.parent, max, None)
                            AVLTreeUpdateHeight(node.left)
                            AVLTreeUpdateHeight(node.right)
                            max.left = node.left
                            max.right = node.right
                            max.parent = node.parent
                            node.left.parent = max
                            node.right.parent = max
                            self.AVLTreeReplaceChild(node.parent , node , max)
                            AVLTreeUpdateHeight(max)
                            parent = node.parent
                            while parent is not None:
                                AVLTreeUpdateHeight(parent)
                                parent = parent.parent
                    else:
                        self.AVLTreeReplaceChild(node.parent , node , None)
                        parent = node.parent
                        while parent is not None:
                            AVLTreeUpdateHeight(parent)
                            parent = parent.parent
                        self.size -= 1
                elif node.parent is None:
                    if node.left is None and node.right is not None:
                        node.right.parent = None
                        self.root = node.right
                        AVLTreeUpdateHeight(self.root)
                        self.size -= 1
                        return node.right
                    elif node.right is None and node.left is not None:
                        node.left.parent = None
                        self.root = node.left
                        AVLTreeUpdateHeight(self.root)
                        self.size -= 1
                        return node.left
                    elif node.right is not None and node.left is not None:
                        max = self.max(node.left)
                        if max.value == node.left.value:
                            max.right = node.right
                            node.right.parent = max
                            max.parent = None
                            AVLTreeUpdateHeight(max.right)
                            AVLTreeUpdateHeight(max)
                            self.root = max
                            self.size -= 1
                        else:
                            self.AVLTreeReplaceChild(max.parent, max, None)
                            AVLTreeUpdateHeight(node.left)
                            AVLTreeUpdateHeight(node.right)
                            max.left = node.left
                            max.right = node.right
                            node.left.parent = max
                            node.right.parent = max
                            max.parent = None
                            AVLTreeUpdateHeight(max)
                            self.root = max
                            self.size -= 1
                    else:
                        self.root = None
                        self.size -= 1
            else:
                return

            node = node.parent
            if node is not None:
                self.AVLTreeRebalance(node)
                if node.parent is not None:
                    self.AVLTreeRebalance(node.parent)
            return node

    def search(self, node, value):
        """
        finds value in avl tree
        :param value: value to find
        :param node: avl tree
        :return: found node
        """

        if node is None:
            return None
        elif node.value == value:
            return node
        elif node.value > value:
            if node.left is not None:
                return self.search(node.left, value)
        elif node.value < value:
            if node.right is not None:
                return self.search(node.right, value)
        return node

    def inorder(self, node):
        """
        puts items in order traversal of avl tree
        :param node: node to traverse
        :return: yields nodes in order
        """
        if node is None:
            print(Node(None).value)
            return Node(None)
        else:
            if node.left is not None:
                yield from self.inorder(node.left)
            yield(node)
            if node.right is not None:
                yield from self.inorder(node.right)
            if node is None:
                print(Node(None).value)
                return Node(None)


    def preorder(self, node):
        """
        puts items in preorder traversal
        :param node: node to traverse
        :return: yields preorder
        """
        if node is None:
            return node
        else:
            yield(node)
            if node.left is not None:
                yield from self.preorder(node.left)
            if node.right is not None:
                yield from self.preorder(node.right)
            if node is None:
                print(Node(None).value)
                return Node(None)

    def postorder(self, node):
        """
        puts items in postorder traversal
        :param node: node to traverse
        :return: yields postorder
        """
        if node is None:
            return node
        else:
            if node.left is not None:
                yield from self.postorder(node.left)
            if node.right is not None:
                yield from self.postorder(node.right)
            yield (node)

    def breadth_first(self, node):
        """
        puts items in breadth first order
        :param node: node to traverse
        :return: yields breadth first order
        """
        #list queue method
        list = []
        if node is None:
            return
        else:
            list.append(node)
            while len(list) is not 0:
                item = list.pop(0)
                yield item
                if item.left is not None:
                    list.append(item.left)
                if  item.right is not None:
                    list.append(item.right)


        # if node is None or self.size == 0:
        #     return node
        # if node == self.root:
        #     yield node
        # if node.left is not None:
        #     yield node.left
        #     if node.right is not None:
        #         yield node.right
        #     yield from self.breadth_first(node.left)
        #     yield from self.breadth_first(node.right)
        # elif node.right is not None:
        #     yield node.right
        #     if node.right is not None:
        #         yield node.right
        #     if node.left is not None:
        #         yield node.left
        #     yield from self.breadth_first(node.left)
        #     yield from self.breadth_first(node.right)




    def depth(self, value):
        """
        finds depth of node
        :param value: value to find
        :return: depth of item
        """
        count = -1
        root = self.root

        if root is None:
            return -1
        else:
            depth1 = self.search(root, value)
            if depth1 is not None:
                while depth1 is not None:
                    count += 1
                    depth1 = depth1.parent
                return count
            else:
                return -1

    def height(self, node):
        """
        finds height of node
        :param node: node to find height of
        :return: returns the height of nide
        """
        if node is None:
            return -1
        return node.height

    def min(self, node):
        """
        finds min in avl tree
        :param node: avl tree to find min in
        :return: min item in tree
        """
        if node is None:
            return None
        elif node.left is not None:
            node = self.min(node.left)
        return node

    def max(self, node):
        """
        finds max in avl tree
        :param node: avl tree to find
        :return: max item in tree
        """
        if node is None:
            return
        elif node.right is not None:
            node = self.max(node.right)
        return node

    def get_size(self):
        """
        returns the size of the item
        """
        return self.size

    def get_balance(self, node):
        """
        gets the balance of a node
        :param node: node to balance
        :return: balance of node
        """
        return self.AVLTreeGetBalance(node)

    def left_rotate(self, root):
        """
        rotate avl tree to the left
        :param root: item to rotate around
        :return: root of subtree
        """
        rightleft = root.right.left  # change to right left

        if root.parent is not None:
            self.AVLTreeReplaceChild(root.parent, root, root.right)
        else:
            self.root = root.right
            self.root.parent = None
        self.AVLTreeSetChild(root.right, "left", root)
        self.AVLTreeSetChild(root, "right", rightleft)
        return root

    def right_rotate(self, root):
        """
        rotate to the right around a node
        :param root: root to rotate around
        :return: subtree node
        """
        leftRight = root.left.right
        if root.parent is not None:
            self.AVLTreeReplaceChild(root.parent, root, root.left)
        else:
            self.root = root.left
            self.root.parent = None
        self.AVLTreeSetChild(root.left, "right", root)
        self.AVLTreeSetChild(root, "left", leftRight)
        return root

    def rebalance(self, node):
        """
        rebalances avl tree
        :param node: node to rebalance
        :return: returns balanced tree
        """
        return self.AVLTreeRebalance(node)

def sum_update(root, total):
    """
    find all items in root tree thats items are larger than it, add them together and insert that into the avl tree
    :param root: root of tree
    :param total: amount to start with
    :return: balanced tree of new nodes
    """
    sum = total
    if root is None:
        return total
    else:
        if root.right is not None:
            sum_update(root.right, sum)

        sum += root.value
        root.value = sum
        sum = total
        if root.left is not None:
            sum_update(root.left , sum)
    # root.AVLTreeRebalance(root)

def AVLTreeUpdateHeight(node):
    """
    updates height of a node
    :param node: node to update
    :return: new height of item
    """
    leftHeight = -1
    rightHeight = -1

    if node.left is not None:
        leftHeight = node.left.height
    if node.right is not None:
        rightHeight = node.right.height
    node.height = max(leftHeight, rightHeight) + 1


if __name__ == '__main__':

    avl = AVLTree()
    avl.insert(avl.root, 10)
    avl.insert(avl.root, 20)
    avl.insert(avl.root, 15)
    avl.insert(avl.root, 25)
    avl.insert(avl.root, 30)
    avl.insert(avl.root, 16)
    print('adsf')

