import random
import matplotlib.pyplot as plt
import numpy as np
import os
os.makedirs("images", exist_ok=True)
import timeit
from bubble_sorts import bubble_sort, bubble_sort_finish_early
from quick_sorts import quick_sort, quick_sort_fast
from merge_sort import merge, merge_sort
from insertion_sort import insertion_sort

def size_plot():
  input_size = np.array([100, 500, 1000, 2000])
  bubble_sort_time = np.array([])
  bubble_sort_finish_early_time = np.array([])
  quick_sort_time = np.array([])
  quick_sort_fast_time = np.array([])
  merge_sort_time = np.array([])
  insertion_sort_time = np.array([])
  
  for i in input_size:
    a = np.random.randint(low=1,high=10000,size=(i))
    
    bubble_sort_time.append(timeit.timeit(lambda: bubble_sort(a), number=100)/100)
    bubble_sort_finish_early_time.append(timeit.timeit(lambda: bubble_sort_finish_early(a), number=100)/100)
    quick_sort_time.append(timeit.timeit(lambda: quick_sort(a), number=100)/100)
    quick_sort_fast_time.append(timeit.timeit(lambda: quick_sort_fast(a), number=100)/100)
    merge_sort_time.append(timeit.timeit(lambda: merge_sort(a), number=100)/100)
    insertion_sort_time.append(timeit.timeit(lambda: insertion_sort(a), number=100)/100)

  plt.plot(input_size, bubble_sort_time, label = Bubble_Sort)
  plt.plot(input_size, bubble_sort_finish_early_time, label = Bubble_Sort_Finish_Early)
  plt.plot(input_size, quick_sort_time, label = Quikc_Sort)
  plt.plot(input_size, quick_sort_fast_time, label = Quick_sort_Fast)
  plt.plot(input_size, merge_sort_time, label = Merge_Sort)
  plt.plot(input_size, insertion_sort_time, label = Insertion_Sort)
  plt.xlabel("Input Size")
  plt.ylabel("NTime taken")
  plt.title("Runtime vs Input Size")
  plt.savefig("images/runtime_vs_input_size.png", dpi=300, bbox_inches="tight")
  plt.show()

size_plot()
