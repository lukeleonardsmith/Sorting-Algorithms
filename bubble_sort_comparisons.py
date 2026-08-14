import numpy as np
import timeit
from bubblesorts import bubble_sort, bubble_sort_finish_early

def bubble_sort_comparison():
  a = np.random.randint(low=1,high=128,size=(100))
  
  bubble_sort_time=timeit.timeit(lambda: bubble_sort(a), number=1)
  bubble_sort_finish_early_time=timeit.timeit(lambda: bubble_sort_finish_early(a), number=1)
            
  print("bubble_sort time: ", bubble_sort_time)                          
  print("bubble_sort_finish_early time: ", bubble_sort_finish_early_time)
  print("Percentage difference in time (with respect to bubble_sort): ,(bubble_sort_finish_early_time - bubble_sort_time)/ubble_sort_time)
  
bubble_sort_comparison()
