def insertion_sort(a):
    
    b = list(a)  # Create a copy to avoid overwriting the contents of a
    n = len(a)
    for k in range(1, n): # Loop for all elements in the list
        x = b[k]
        j = k - 1
        while (j >= 0) and (b[j] > x): # Find the point in the list where every element to the right is greater than the chosen element
            b[j + 1] = b[j]
            j = j - 1
        b[j + 1] = x # Insert the element here
    return b
