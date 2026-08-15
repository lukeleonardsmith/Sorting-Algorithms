def quick_sort(a):
    small = []
    middle = []
    big = []
    if len(a) == 1:  
        return a
    elif len(a) == 2:
        if a[0] > a[1]:
            b = list(a)
            a[0] = b[1]
            a[1] = b[0]
            return a
        else:
            return a
    else:
        for k in range (0, len(a)):
            if a[k] < a[len(a)//2]:
                small.append(a[k])
            elif a[k] > a[len(a)//2]:
                big.append(a[k])
            elif a[k] == a[len(a)//2]:
                middle.append(a[k])
    if len(small) == 0 and len(big) == 0:
        return middle
    elif len(small) == 0:
        return middle + quick_sort(big)
    elif len(big) == 0:
        return quick_sort(small) + middle
    return quick_sort(small) + middle + quick_sort(big)

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
            return a.reverse()  
        else:
            return a
    else:
        length = len(a)
        alengthover2 = a[len(a)//2]
        for k in range (0, length):
            ak = a[k]
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
