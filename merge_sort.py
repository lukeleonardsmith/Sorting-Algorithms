def merge(a1, a2):
    """Merge two sorted lists a1 and a2 and return merged list

    input:
        a1 = first sorted list
        a2 = second sorted list
    output:
        sorted list containing all elements from a1 and a2
    """
    a = []
    while (len(a1) > 0) and (len(a2) > 0):
        # Pick the smaller of the two elements
        if a1[0] < a2[0]:
            a.append(a1.pop(0))
        else:
            a.append(a2.pop(0))
    # Append the remaining elements of either a1 or a2 to the final list
    # (only one of these lines will actually do something)
    a += a1
    a += a2
    return a

def merge_sort(a):
    """Sort the list a in ascending order and return sorted list

    input:
        a = unsorted list
    output:
        sorted list containing all elements from a
    """
    n = len(a)
    if n <= 1:
        return a
    else:
        a1 = a[: n // 2]
        a2 = a[n // 2 :]
        return merge(merge_sort(a1), merge_sort(a2))
