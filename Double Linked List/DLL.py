"""
CSE 331 Project 1
Author: *your name here*
"""

class DLLNode:
    """
    Class representing a node in the doubly linked list implemented below.
    """

    def __init__(self, value, next = None, prev = None):
        """
        Constructor
        @attribute value: the value to give this node
        @attribute next: the next node for this node
        @attribute prev: the previous node for this node
        """
        self.__next = next
        self.__prev = prev
        self.__value = value

    def __repr__(self):
        return str(self.__value)

    def __str__(self):
        return str(self.__value)

    def get_value(self):
        """
        Getter for value
        :return: the value of the node
        """
        return self.__value

    def set_value(self, value):
        """
        Setter for value
        :param value: the value to set
        """
        self.__value = value

    def get_next(self):
        """
        Getter for next node
        :return: the next node
        """
        return self.__next

    def set_next(self, node):
        """
        Setter for next node
        :param node: the node to set
        """
        self.__next = node

    def get_previous(self):
        """
        Getter for previous node
        :return: the previous node
        """
        return self.__prev

    def set_previous(self, node):
        """
        Setter for previous node
        :param node: the node to set
        """
        self.__prev = node

class DLL:
    """
    Class representing a doubly linked list.
    """
    def __init__(self):
        """
        Constructor
        @attribute head: the head of the linked list
        @attribute tail: the tail of the linked list
        @attribute size: the size of the linked list
        """
        self.head = None
        self.tail = None
        self.size = 0

    def __repr__(self):
        """
        iterates through the linked list to generate a string representation
        :return: string representation of the linked list
        """
        res = ""
        node = self.head
        while node:
            res += str(node)
            if node.get_next():
                res += " "
            node = node.get_next()
        return res

    def __str__(self):
        """
        iterates through the linked list to generate a string representation
        :return: string representation of the linked list
        """
        res = ""
        node = self.head
        while node:
            res += str(node)
            if node.get_next():
                res += " "
            node = node.get_next()
        return res

    ######### MODIFY BELOW ##########

    def get_size(self):
        """
        Gives the user the size of their linked list
        :return: [int] the size of the linked list
        """
        return self.size

    def is_empty(self):
        """
        Determines if the linked list is empty or not
        :return: [boolean] true if DLL is empty, false otherwise
        """
        if self.get_size() == 0:
            return True
        return False

    def insert_front(self, value):
        """
        Inserts a value into the front of the list
        :param value: the value to insert
        """

        valueNode = DLLNode(value)
        node = self.head

        if self.get_size() == 0:
            self.head = valueNode
            self.tail = valueNode
            self.size += 1

            return self

        self.size += 1
        node.set_previous(valueNode)
        valueNode.set_next(node)
        self.head = valueNode

        return self

    def insert_back(self, value):
        """
        Inserts a value into the back of the list
        :param value: the value to insert
        """
        valueNode = DLLNode(value)
        node = self.head

        if self.get_size() == 0:
            self.size += 1
            self.head = valueNode
            self.tail = valueNode
            return self


        while node.get_next() != None:
            node = node.get_next()

        self.size += 1
        valueNode.set_previous(node)
        node.set_next(valueNode)
        self.tail = valueNode

        return self

    def delete_front(self):
        """
        Deletes the front node of the list
        """
        node = self.head

        if self.get_size() == 0:
            return self

        if self.get_size() == 1:
            self.head = None
            self.tail = None
            self.size -= 1
            return self

        nextNode = node.get_next()
        nextNode.set_previous(None)
        self.head = nextNode
        self.size -= 1
        return self

    def delete_back(self):
        """
        Deletes the back node of the list
        """
        node = self.head

        if self.get_size() == 0:
            return self

        print(self.get_size())

        if self.get_size() == 1:

            self.head = None
            self.tail = None
            self.size -= 1
            return self

        while node.get_next() != None:
            node = node.get_next()
        secondLast = node.get_previous()
        secondLast.set_next(None)
        node.set_previous(None)
        self.tail = secondLast
        self.size -= 1
        return self

    def delete_value(self, value):
        """
        Deletes the first instance of the value in the list.
        :param value: The value to remove
        """
        node = self.head
        while node != None:
            if node.get_value() == value:
                if self.get_size() == 1:
                    self.head = None
                    self.tail = None
                    self.size -= 1
                    return self
                if node.get_next() == None:
                    previousNode = node.get_previous()
                    previousNode.set_next(None)
                    self.tail = previousNode
                    self.size -= 1
                    return self

                if node.get_previous() == None:
                    nextNode = node.get_next()
                    nextNode.set_previous(None)
                    self.head = nextNode
                    self.size -= 1
                    return self

                previousNode = node.get_previous()
                nextNode = node.get_next()
                previousNode.set_next(nextNode)
                nextNode.set_previous(previousNode)
                self.size -= 1
                return self
            node = node.get_next()
        return self


    def delete_all(self, value):
        """
        Deletes all instances of the value in the list
        :param value: the value to remove
        """
        node = self.head
        while node != None:
            if node.get_value() == value:
                if self.get_size() == 1:
                    self.head = None
                    self.tail = None
                    self.size -= 1

                elif node.get_next() == None:
                    previousNode = node.get_previous()
                    previousNode.set_next(None)
                    self.tail = previousNode
                    self.size -= 1


                elif node.get_previous() == None:
                    nextNode = node.get_next()
                    nextNode.set_previous(None)
                    self.head = nextNode
                    self.size -= 1

                else:
                    previousNode = node.get_previous()
                    nextNode = node.get_next()
                    previousNode.set_next(nextNode)
                    nextNode.set_previous(previousNode)
                    self.size -= 1

            node = node.get_next()

        return self


    def find_first(self, value):
        """
        Finds the first instance of the value in the list
        :param value: the value to find
        :return: [DLLNode] the first node containing the value
        """
        node = self.head
        while node != None:
            if node.get_value() == value:
                return node
            node = node.get_next()
        return None

    def find_last(self, value):
        """
        Finds the last instance of the value in the list
        :param value: the value to find
        :return: [DLLNode] the last node containing the value
        """
        endNode = self.tail
        while endNode != None:
            if endNode.get_value() == value:
                return endNode
            endNode = endNode.get_previous()
        return None

    def find_all(self, value):
        """
        Finds all of the instances of the value in the list
        :param value: the value to find
        :return: [List] a list of the nodes containing the value
        """
        node = self.head
        nodeList = []
        while node != None:
            if node.get_value() == value:
                nodeList.append(node)
            node = node.get_next()
        return nodeList

    def count(self, value):
        """
        Finds the count of times that the value occurs in the list
        :param value: the value to count
        :return: [int] the count of nodes that contain the given value
        """
        count = 0
        node = self.head
        while node != None:
            if node.get_value() == value:
                count += 1
            node = node.get_next()
        return count

    def sum(self):
        """
        Finds the sum of all nodes in the list
        :param start: the indicator of the contents of the list
        :return: the sum of all items in the list
        """
        if self.get_size() == 0:
            return None

        node = self.head
        sum = node.get_value()

        node = node.get_next()
        while node != None:
            sum += node.get_value()
            node = node.get_next()

        return sum

def remove_middle(LL):
    """
    Removes the middle of a given doubly linked list.
    :param DLL: The doubly linked list that must be modified
    :return: The updated linked list
    """
    middleCounter = 0
    node = LL.head
    midLocation = LL.get_size() // 2
    if LL.get_size() < 3:
        return DLL()
    else:
        while node != None:
            if middleCounter == midLocation:
                break
            node = node.get_next()
            middleCounter += 1

        if LL.get_size() % 2 != 0:
            previousNode = node.get_previous()
            nextNode = node.get_next()
            previousNode.set_next(nextNode)
            nextNode.set_previous(previousNode)
            LL.size -= 1
            return LL
        else:
            previousNode = node.get_previous().get_previous()
            nextNode = node.get_next()
            previousNode.set_next(nextNode)
            nextNode.set_previous(previousNode)
            LL.size -= 2
            return LL

