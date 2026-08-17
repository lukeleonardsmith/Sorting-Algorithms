def quick_sort(a):
    small = []
    middle = []
    big = []
    if len(a) == 1:  
        return a # If a list only has one element is is sorted
    elif len(a) == 2:
        if a[0] > a[1]:
            b = list(a)
            a[0] = b[1]
            a[1] = b[0]
            return a # If a list has two elements and it is unordered, swapping the elements around will sort it
        else:
            return a # If both elemnts are sorted, then all elements are sorted
    else:
        for k in range (0, len(a)):
            if a[k] < a[len(a)//2]:
                small.append(a[k]) # All elements with a value less than the middle value in the list is appended to a new list called small
            elif a[k] > a[len(a)//2]:
                big.append(a[k]) # All elements with a value greater than the middle value in the list is appended to a new list called big
            elif a[k] == a[len(a)//2]:
                middle.append(a[k]) # The elements with an equal value are appended to a list called middle
    if len(small) == 0 and len(big) == 0:
        return middle # If both small and big are empty, return middle as all elements have the same value, so any order is sorted
    elif len(small) == 0:
        return middle + quick_sort(big) # As no elements in small, the sorted list is middle and then the sorted version of big
    elif len(big) == 0:
        return quick_sort(small) + middle # As no elements in big, the sorted list is and the sorted version of small and then middle
    return quick_sort(small) + middle + quick_sort(big) # When small and big are sorted, pace middle between them and then the list is sorted. This will work recursively as at a point, the sub lists will be either length one or two, which are shown how to sort

'''
Below is an alterate version which has been changed to be as time efficient as possible.
'''

def quick_sort_fast(a):
    small = []
    middle = []
    big = []
    if len(a) == 1:  
        return a
    elif len(a) == 2:
        if a[0] > a[1]:
            a.reverse() # The inbuilt reverse function is more effective than running more code
            return a  
        else:
            return a
    else:
        length = len(a)
        alengthover2 = a[len(a)//2] # By doing this, a[len(a)//2] is ont needlessly recalculated
        for k in range (0, length):
            ak = a[k] # By doing this, a[k] is not needlessly recalculated
            if ak < alengthover2:
                small.append(ak)
            elif ak > alengthover2:
                big.append(ak)
            else:
                middle.append(ak)
    if len(small) == 0 and len(big) == 0:
        return middle
    elif len(small) == 0:
        return middle + quick_sort_fast(big)
    elif len(big) == 0:
        return quick_sort_fast(small) + middle
    return quick_sort_fast(small) + middle + quick_sort_fast(big)
