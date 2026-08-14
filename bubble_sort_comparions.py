import numpy as np
from bubblesorts import bubble_sort, bubble_sort_finish_early

def bubble_sort_comparison():
  a = np.random.randint(low=1,high=128,size=(100))
  
  print(a)
  print(bubble_sort(a))
  print(bubble_sort_finish_early(a))
  %timeit bubble_sort(a)
  %timeit bubble_sort_finish_early(a)
