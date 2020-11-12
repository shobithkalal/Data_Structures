from string import ascii_lowercase


class Node:
    """
    Node definition should not be changed in any way
    """
    __slots__ = ['_key', '_value']

    def __init__(self, k, v):
        """
        Initializes node
        :param k: key to be stored in the node
        :param v: value to be stored in the node
        """
        self._key = k
        self._value = v

    def __lt__(self, other):
        """
        Less than comparator
        :param other: second node to be compared to
        :return: True if the node is less than other, False if otherwise
        """
        return self._key < other.get_key() or (self._key == other.get_key() and self._value < other.get_value())

    def __gt__(self, other):
        """
        Greater than comparator
        :param other: second node to be compared to
        :return: True if the node is greater than other, False if otherwise
        """
        return self._key > other.get_key() or (self._key == other.get_key() and self._value > other.get_value())

    def __eq__(self, other):
        """
        Equality comparator
        :param other: second node to be compared to
        :return: True if the nodes are equal, False if otherwise
        """
        return self._key == other.get_key() and self._value == other.get_value()

    def __str__(self):
        """
        Converts node to a string
        :return: string representation of node
        """
        return '({0},{1})'.format(self._key, self._value)

    __repr__ = __str__

    def get_key(self):
        """
        Key getter function
        :return: key value of the node
        """
        return self._key

    def set_key(self, new_key):
        """
        Key setter function
        :param new_key: the value the key is to be changed to
        """
        self._key = new_key

    def get_value(self):
        """
        Value getter function
        :return: value of the node
        """
        return self._value


class PriorityHeap:
    """
    Partially completed data structure. Do not modify completed portions in any way
    """
    __slots__ = '_data'

    def __init__(self):
        """
        Initializes the priority heap
        """
        self._data = []

    def __str__(self):
        """
        Converts the priority heap to a string
        :return: string representation of the heap
        """
        return ', '.join(str(item) for item in self._data)

    def __len__(self):
        """
        Length override function
        :return: Length of the data inside the heap
        """
        return len(self._data)

    __repr__ = __str__

    #   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #   Modify below this line

    def empty(self):
        """
        figures out if the the queue is empty
        :return: true if empty, false if not
        """
        if self.__len__() == 0:
            return True
        else:
            return False

    def top(self):
        """
        finds the root item of the queue
        :return: returns the top item of the queue
        """
        if self.empty() is True:
            return None
        else:
            if self._data[0] is None:
                return None
            return self._data[0].get_value()

    def push(self, key, val):
        """
        adds and item to the queue and places it approperlty
        :param key: key of the node
        :param val: value of the node
        :return: none if there is no key
        """
        if key is None:
            return None
        self._data.append(Node(key, val))
        self.percolate_up(self.__len__() - 1)

    def pop(self):
        """
        deletes the root node and properly reset queue
        :return: the root node
        """
        if self.empty():
            return
        self.swap(0, len(self._data) - 1)
        minimum = self._data.pop()
        self.percolate_down(0)
        return minimum

    def min_child(self, index):
        """
        finds the minimum child given the index of the parent
        :param index: index of parent
        :return: returns the smallest child
        """
        if self.has_left(index) is True:
            smallest = self.left(index)
            if self.has_right(index):
                right = self.right(index)
                if self._data[smallest] > self._data[right]:
                    smallest = right
            return smallest
        else:
            return None

    def percolate_up(self, index):
        """
        percolates an item up to its proper location in min heap
        :param index: index of item to percolate up
        :return: no return
        """
        while index > 0:
            parent = (index - 1) // 2
            if self._data[index] < self._data[parent] and index > 0:
                self.swap(index, parent)
                index = parent
            else:
                return

    def percolate_down(self, index):
        """
        percolates an item down to its proper location in min heap
        :param index: index of item to move
        :return: no return
        """
        if self.has_left(index) is True:
            smallest = self.left(index)
            if self.has_right(index):
                right = self.right(index)
                if self._data[smallest] > self._data[right]:
                    smallest = right
            if self._data[smallest] < self._data[index]:
                self.swap(index, smallest)
                self.percolate_down(smallest)

    def change_priority(self, index, new_key):
        """
        changes the priority of an item given the index
        :param index: index of item to change priority on
        :param new_key: new key to change value too
        :return: no return
        """
        if index >= len(self._data) or self.empty() is True:
            return
        old_key = self._data[index].get_key()
        self._data[index].set_key(new_key)

        if new_key > old_key:
            self.percolate_down(index)
        elif new_key < old_key:
            self.percolate_up(index)

    def swap(self, pos1, pos2):
        """
        swap two items in a list
        :param pos1: postion of first item
        :param pos2: positio of second item
        :return: returns the swapped list
        """
        self._data[pos1], self._data[pos2] = self._data[pos2], self._data[pos1]

    def parent(self, index):
        """
        finds parent of item
        :param index: index of item to find parent of
        :return: parent location of item
        """
        return (index - 1) // 2

    def left(self, index):
        """
        finds left child of item
        :param index: index of item to look at
        :return: returns the left child
        """
        return 2 * index + 1

    def right(self, index):
        """
        finds right child of item
        :param index: index of item to look at
        :return: returns the right child
        """
        return 2 * index + 2

    def has_left(self, index):
        """
        if the left child is within the list
        :param index: index of item to look at
        :return: returns true if there is a child, False if no child
        """
        return self.left(index) < len(self._data)

    def has_right(self, index):
        """
        if the right child is within the list
        :param index: index of item to look at
        :return: returns true if there is a child, False if no child
        """
        return self.right(index) < len(self._data)


def swap(self, pos1, pos2):
    """
    swap two items in a list
    :param pos1: postion of first item
    :param pos2: positio of second item
    :return: returns the swapped list
    """
    self[pos1], self[pos2] = self[pos2], self[pos1]


def parent(index):
    """
    finds parent of item
    :param index: index of item to find parent of
    :return: parent location of item
    """
    return (index - 1) // 2


def left(index):
    """
    finds left child of item
    :param index: index of item to look at
    :return: returns the left child
    """
    return 2 * index + 1


def right(index):
    """
    finds right child of item
    :param index: index of item to look at
    :return: returns the right child
    """
    return 2 * index + 2


def has_left(self, index):
    """
    if the left child is within the list
    :param index: index of item to look at
    :return: returns true if there is a child, False if no child
    """
    return left(index) < len(self)


def has_right(self, index):
    """
    if the right child is within the list
    :param index: index of item to look at
    :return: returns true if there is a child, False if no child
    """
    return right(index) < len(self)


def MaxHeapPercolateDown(array, index, size):
    """
    used for heap_sort. basically heapifys a list into a max heap
    :param array: array to heapify
    :param index: index of item that needs to be moved
    :return: no return
    """
    leftChild = left(index)
    rightChild = right(index)

    if leftChild < size and array[leftChild] > array[index]:
        largest = leftChild
    else:
        largest = index
    if rightChild < size and array[rightChild] > array[largest]:
        largest = rightChild
    if largest is not index:
        swap(array, index, largest)
        MaxHeapPercolateDown(array, largest, size)


def heap_sort(array):
    """
    sorts an array using a max heap
    :param array: array to sort
    :return: returns sorted array
    """

    for index in range(int(len(array) / 2) - 1, -1, -1):
        MaxHeapPercolateDown(array, index, len(array))
    for index2 in range(len(array) - 1, -1, -1):
        swap(array, 0, index2)
        MaxHeapPercolateDown(array, 0, index2)
    return array


def merge_lists(array_list):
    """
    merges the list using a min heap and sorts it using heap sort
    :param array_list: the list of arrays to sort
    :return: returns sorted merged array
    """
    if array_list is None:
        return
    minHeap = PriorityHeap()
    for arrayNum in range(len(array_list)):
        if len(array_list[arrayNum]) != 0:
            poped = array_list[arrayNum].pop()
            minHeap.push(arrayNum, poped)
    finalArray = []
    while minHeap.__len__() is not 0:
        head = minHeap.pop()
        if head.get_value() not in finalArray:
            finalArray.append(head.get_value())
        if len(array_list[head.get_key()]) != 0:
            minHeap.push(head.get_key(), array_list[head.get_key()].pop())
    return heap_sort(finalArray)


if __name__ == "__main__":
    lists = [[1], [1]]
    merged = merge_lists(lists)
    print(merged)
