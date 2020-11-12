"""
PROJECT 3 - Quick/Insertion Sort
Name:
PID:
"""

from Project3.InsertionSort import insertion_sort


# from InsertionSort import insertion_sort


def quick_sort(dll, start, end, size, threshold):
    """
    quick sort technique of sorting
    :param dll: doubly linked list passed in
    :param start: start node to iterate at
    :param end: end node to stop iteration at
    :param size: size of DLL
    :param threshold: amount to be under to call Insertion Sort
    :return: returns the sorted list
    """
    j = 0
    if start is None or size == 1:
        return dll
    if size <= threshold:
        insertion_sort(dll, start, end)
    else:
        j = partition(start, end)
        quick_sort(dll, start, j[0].get_previous(), j[1], threshold)
        quick_sort(dll, j[0].get_next(), end, size - j[1], threshold)


#
#
# j = 0
# if start.get_value() >= end.get_value():
#     return dll
# j = partition(start , end)
# quick_sort(dll , start , j[0].get_previous() , j[1] , threshold)
# quick_sort(dll , j[0].get_next() , end , j[1] , threshold)
# return dll


def partition(low, high):
    """
    split the linked list for quick sort
    :param low: low node to start iteration at
    :param high: high node to stop iteration at
    :return: returns the low node as well as size
    """
    pivot = high
    left = low
    right = low
    size = 0
    while right is not pivot.get_next() and right.get_next() is not None:
        if right.get_value() >= pivot.get_value():
            right = right.get_next()
        else:
            temp = left.get_value()
            left.set_value(right.get_value())
            right.set_value(temp)
            left = left.get_next()
            right = right.get_next()
            size += 1
    temp = left.get_value()
    left.set_value(pivot.get_value())
    pivot.set_value(temp)
    size += 1
    return left, size

    # size = 0
    # high = high.get_previous()
    # while True:
    #     # while low is not high and low.get_value() < pivot.get_value():
    #     #     low = low.get_next()
    #     #     size += 1
    #
    #     while low is not high and high.get_value() > pivot.get_value():
    #         high = high.get_previous()
    #
    #     if low.get_value() > high.get_value():
    #         break
    #
    #     else:
    #         temp = low.get_value()
    #         low.set_value(high.get_value())
    #         high.set_value(temp)
    # return high

    # pivot = high
    # current = high.get_previous()
    # low = low
    # size = 0
    # while low is not current:
    #     while low is not current and low.get_value() < pivot.get_value():
    #         low = low.get_next()
    #         size += 1
    #     while current is not low and current.get_value() > pivot.get_value():
    #         current = current.get_previous()
    #     if low is not current.get_previous():
    #         temp = low.get_value()
    #         low.set_value(current.get_value())
    #         current.set_value(temp)
    #     current = current.get_previous()
    #     low = low.get_next()
    # temp = low.get_value()
    # low.set_value(pivot.get_value())
    # pivot.set_value(temp)
    # size += 1
    # return (low , size)

    # create pivot point based on high point
    # if high.get_value() < low.get_value():
    #     return
    #
    # pivot = high.get_value()
    # pivotNode = high
    # high = high.get_previous()
    # size = 0
    # while low is not high:
    #     while low is not high and low.get_value() < pivot:
    #         low = low.get_next()
    #         size += 1
    #     while low is not high and high.get_value() > pivot:
    #         high = high.get_previous()
    #     if low.get_value() <= high.get_value():
    #         temp = low.get_value()
    #         low.set_value(high.get_value())
    #         high.set_value(temp)
    #         low = low.get_next()
    #
    #     temp = low.get_value()
    #     low.set_value(pivot)
    #     pivotNode.set_value(temp)
    #     size += 1
    #     low = low.get_next()
    #     high = high.get_previous()
    # tuple1 = (low , size)
    # return tuple1


