"""
PROJECT 2 - Linked List Recursion
Name:
PID:
"""


class LinkedNode:
    # DO NOT MODIFY THIS CLASS #
    __slots__ = 'value', 'next'

    def __init__(self, value, next=None):
        """
        DO NOT EDIT
        Initialize a node
        :param value: value of the node
        :param next: pointer to the next node in the LinkedList, default is None
        """
        self.value = value  # element at the node
        self.next = next  # reference to next node in the LinkedList

    def __repr__(self):
        """
        DO NOT EDIT
        String representation of a node
        :return: string of value
        """
        return str(self.value)

    __str__ = __repr__


# IMPLEMENT THESE FUNCTIONS - DO NOT MODIFY FUNCTION SIGNATURES #


def insert(value, node=None):
    '''
    Inserts a given node of a value to the front of a linked list
    :param value: value to insert into linked list
    :param node: node passed into to connect to or create new node
    :return: head node of list
    '''
    if node is None:
        return LinkedNode(value)
    else:
        node.next = insert(value, node.next)
    return node

def to_string(node):
    '''
    convert linked list to string
    :param node: linked list to print
    :return: linked list converted to string
    '''
    try:
        if node.next is not None:
            return str(node.value) + ", " + to_string(node.next)
        else:
            return str(node.value)
    except:
        return ""

def remove(value, node):
    '''
    removes a node of a given value
    :param value: value of node to delete
    :param node: list passed in
    :return: returns head node
    '''
    if node is None:
        return node

    elif node.value == value:
        return node.next
    else:
        node.next = remove(value, node.next)
        return node


def remove_all(value, node):
    '''
    removes all instances of a value
    :param value: value to delete
    :param node: linked list passed in
    :return: returns head node
    '''
    if node is None:
        return node
    if node.value == value:
        return remove_all(value , node.next)
    else:
        node.next = remove_all(value, node.next)
        return node


def search(value, node):
    '''
    sees if a value is in a linked list
    :param value: value to search for
    :param node: linked list passed in
    :return: returns true or false if value is located
    '''
    if node is None:
        return False
    elif node.value == value:
        return True
    else:
        return search(value, node.next)


def length(node):
    '''
    finds the length of a linked list
    :param node: head node of a linked list
    :return: length of the linked list
    '''
    if node is None:
        return 0
    if node.next is None:
        return 1
    else:
        return 1 + length(node.next)


def sum_list(node):
    '''
    sums all values of nodes in a linked list
    :param node: head of linked list
    :return: returns sum of all nodes in linked list
    '''
    if node is None:
        return 0
    if node.next is None:
        return node.value
    else:
        return node.value + sum_list(node.next)

def count(value, node):
    '''
    counts how many nodes of a value are presents in a linked list
    :param value: value to look for
    :param node: head node of linked list
    :return: returns the num of times a value occurs in a linked list
    '''
    if node is None:
        return 0
    if node.value == value:
        return 1 + count(value, node.next)
    else:
        return count(value, node.next)

def reverse(node):
    '''
    reverses order of a linked list
    :param node: head node of a linked list
    :return: returns the new head node of reversed linked list
    '''
    if node is None:
        return node
    if node.next is None:
        return node
    else:
        nextNode = node.next
        headNode = reverse(node.next)
        nextNode.next = node
        node.next = None
        return headNode

def remove_fake_requests(head):
    '''
    remove all non unique items within a linked list
    :param head: head of linked list
    :return: returns linked list of all unique items
    '''

    if head is None or head.next is None:
        return head
    if head.value == head.next.value:
        return remove_fake_requests(remove_all(head.value, head))
    else:
        head.next = remove_fake_requests(head.next)
        return head

    #only had this working for first test case, this was the attempt to make O(n) instead of O(n^2)
    # if head is None:
    #     return head
    # if head.value == head.next.value:
    #     while head.value == head.next.value:
    #         head.next = head.next.next
    #     head = head.next
    #     return remove_fake_requests(head.next)
    # else:
    #     head.next = remove_fake_requests(head.next)
    #     return head



if __name__ == "__main__":
    requests = insert(170144)
    insert(567384, requests)
    insert(604853, requests)
    insert(783456, requests)
    insert(783456, requests)
    insert(903421, requests)
    real_requests = remove_fake_requests(requests)
    for i in [170144, 567384, 604853, 903421]:
        assert real_requests.value == i
        real_requests = real_requests.next


