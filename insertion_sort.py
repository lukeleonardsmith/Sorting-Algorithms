def insertion_sort(a):
    """Sort a list using Insertion Sort

    input: list a
    output: rearrangement of the list a in ascending order
    """
    b = list(a)  # Create a copy to avoid overwriting the contents of a
    n = len(a)
    for k in range(1, n):
        x = b[k]
        j = k - 1
        while (j >= 0) and (b[j] > x):
            b[j + 1] = b[j]
            j = j - 1
        b[j + 1] = x
    return b
