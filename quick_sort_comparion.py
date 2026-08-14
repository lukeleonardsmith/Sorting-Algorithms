import numpy as np
import timeit
from quicksorts import quick_sort, quick_sort_fast

def quick_sort_comparisons():
  a = np.random.randint(low=1,high=128,size=(100))
  
  quick_sort_time=timeit.timeit(lambda: quick_sort(a), number=1)
  quick_sort_fast_time=timeit.timeit(lambda: quick_sort_fast(a), number=1)
            
  print("quick_sort time: ", quick_sort_time)                          
  print("quick_sort_fast time: ", bubble_sort_fast_time)
  print("Percentage difference in time (with respect to quick_sort): ", (quick_sort_fast_time - quick_sort_time)/quick_sort_time, "%")
  
quick_sort_comparison()
