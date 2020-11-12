"""
PROJECT 3 - Quick/Insertion Sort
Name:
PID:
"""


def _insertion_wrapper(insertion_sort):
    """
    DO NOT EDIT
    :return:
    """

    def insertion_counter(*args, **kwargs):
        if args[0].size > 1:
            args[0].c += 1
        insertion_sort(*args, **kwargs)

    return insertion_counter


# ------------------------Complete function below---------------------------
@_insertion_wrapper
def insertion_sort(dll, low, high):
    """
    goes through and sorts based on insertin sort
    :param dll: doubly linked list passed in
    :param low: low node to start iteration at
    :param high: high node to stop iteration at
    :return: returns the sorted list
    """
    if dll.get_size() == 1 or dll.get_size() == 0:
        return
    next = low.get_next()

    while next is not None and next is not high.get_next():
        current = next.get_previous()
        # if current.get_value() == next.get_value():
        #     current = current.get_previous()
        while current is not None and current is not low.get_previous():
            if next.get_value() < current.get_value():
                # if current.get_value() == next.get_value():
                #     current = current.get_previous()
                temp = next.get_value()
                next.set_value(current.get_value())
                current.set_value(temp)
                next = current
            current = current.get_previous()
        next = next.get_next()

    # swapping values method
    # current = low.get_next() #second item in list when initilized
    # while current is not None and current is not high:
    #     current = current
    #     previous = current.get_previous()
    #     next  = current.get_next()
    #     while current is not None and current.get_value() < previous.get_value():
    #         previous = previous.get_previous()
    #     previous.set_next(next)
    #     if current.get_next() is not None:
    #         next.set_previous(previous)
    #     elif previous is None:
    #         previous = low
    #         current.set_previous(None)
    #         current.set_next(previous)
    #         current.get_next.set_previous(current)
    #     else:
    #         previous = prevoius.get_next()
    #         previous.get_previous().set_next(previous)
    #         current.set_previous(previous.get_previous())

    # creating new DLL and add to that attempt
    # sorted = DLL(None)
    #
    # while low is not None and low is not high:
    #     next = DLLNode(low.get_value())
    #
    #     if sorted.get_head() is None:
    #         sorted.set_head(next)
    #         print(sorted)
    #     elif sorted.get_head().get_value() >= next.get_value():
    #         next.set_next(sorted.get_head())
    #         sorted.get_head().set_previous(next)
    #         sorted.set_head(next)
    #         print(sorted)
    #     else:
    #         current = sorted.get_head()
    #         while current.get_next() is not None and current.get_next().get_value() < next.get_value():
    #             current = current.get_next()
    #         next.set_next(current.get_next())
    #         if current.get_next() is not None:
    #             next.get_next().set_previous(next)
    #         current.set_next(next)
    #         next.set_previous(current)
    #
    #     low = low.get_next()
    #
    # return sorted


if __name__ == "__main__":
    orig = [2, 1, -2, 4, -5, -1]
    dll = DLL(orig)
    print(dll)
    print("----------------------------------")
    print(DLL(sorted(orig)))
    insertion_sort(dll, dll.get_head(), dll.get_tail())
    print(dll)
    print("fuck me")
