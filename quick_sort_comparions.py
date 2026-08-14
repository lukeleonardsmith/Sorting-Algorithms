import numpy as np
import timeit
from quicksorts import quick_sort, quick_sort_fast

def quick_sort_comparisons():
  a = np.random.randint(low=1,high=128,size=(100))

print(a)
print(quick_sort(a))
print(quick_sort_fast(a))
%timeit quick_sort(a)
%timeit quick_sort_fast(a)
