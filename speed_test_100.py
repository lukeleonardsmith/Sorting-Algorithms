import numpy as np
import timeit
from bubble_sorts import bubble_sort, bubble_sort_finish_early
from quick_sorts import quick_sort, quick_sort_fast
from merge_sort import merge, merge_sort

def speed_test_100():
  a = list(np.random.randint(low=1,high=128,size=(100)))
  
  bubble_sort_time=timeit.timeit(lambda: bubble_sort(a), number=1)
  bubble_sort_finish_early_time=timeit.timeit(lambda: bubble_sort_finish_early(a), number=1) 
  quick_sort_time=timeit.timeit(lambda: quick_sort(a), number=1)
  quick_sort_fast_time=timeit.timeit(lambda: quick_sort_fast(a), number=1)
  merge_sort_time=timeit.timeit(lambda: merge_sort(a), number=1)

  print("bubble_sort time: ", bubble_sort_time)                          
  print("bubble_sort_finish_early time: ", bubble_sort_finish_early_time)
  print("quick_sort time: ", quick_sort_time)                          
  print("quick_sort_fast time: ", quick_sort_fast_time)
  print("merge_sort time: ", merge_sort_time)                         
  
speed_test_100()
