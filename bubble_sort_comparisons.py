import numpy as np
import timeit
from bubblesorts import bubble_sort, bubble_sort_finish_early

def bubble_sort_comparison():
  a = np.random.randint(low=1,high=128,size=(100))
  
  print(a)
  print(bubble_sort(a))
  print(bubble_sort_finish_early(a))
  print("bubble_sort time:")
  print(timeit.timeit(lambda: bubble_sort(a)))
  print("bubble_sort_finish_early time:")
  print(timeit.timeit(lambda: bubble_sort_finish_early(a)))
  print("Percentage difference in time:")
  print(((timeit.timeit(lambda: bubble_sort_finish_early(a)) - timeit.timeit(lambda: bubble_sort_finish_early(a)))/timeit.timeit(lambda: bubble_sort_finish_early(a))*100, "%")
