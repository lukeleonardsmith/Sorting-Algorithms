def bubble_sort(a):
    b = list(a)
    for n in range (0, len(a)-1):
        for k in range (0, len(a)-1):
            if b[k] > b[k+1]:
                c = list(b)
                b[k] = c[k+1]
                b[k+1] = c[k]
    return b

'''
Alternate version which checks if the list is unchanged and hence sorted after an iteration, leading to the list being outputted, ending all loops. 
This can be quicker, yet also adds an extra if statement for every iteration.
'''
def bubble_sort_finish_early(a):
    b = list(a)
    iteration_before = []
    iteration_after = [1]
    for n in range (0, len(a)-1):
        if iteration_after == iteration_before:
            break
        else:
            iteration_before = list(b)
            for k in range (0, len(a)-1):
                if b[k] > b[k+1]:
                    c = list(b)
                    b[k] = c[k+1]
                    b[k+1] = c[k]
            iteration_after = list(b)
    return b
