def merge(a1, a2):
    
    a1 = list(a1)
    a2 = list(a2)
    a = []
    while (len(a1) > 0) and (len(a2) > 0):
        # Pick the smaller of the two elements and append it to the smaller of an empty list
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

    n = len(a)
    if n <= 1: # List is sorted if only one element
        return a
    else:
        a1 = a[: n // 2] # Split the list in two
        a2 = a[n // 2 :]
        return merge(merge_sort(a1), merge_sort(a2)) # Recursively call merge_sort until merging single entries
