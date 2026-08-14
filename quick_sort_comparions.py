import numpy as np

def quick_sort_comparisons():
  a = np.random.randint(low=1,high=128,size=(100))

print(a)
print(quick_sort(a))
print(quick_sort_fast(a))
%timeit quick_sort(a)
%timeit quick_sort_fast(a)
