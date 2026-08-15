import numpy as np
from bubble_sorts import bubble_sort, bubble_sort_finish_early
from quick_sorts import quick_sort, quick_sort_fast
from merge_sort import merge, merge_sort

def examples():
  print("The following are each respective sorting algorithms sorting unique lists of 100 random integers.")
  print()
  bubble_sort_example()
  print()
  bubble_sort_finish_early_example()
  print()
  quick_sort_example()
  print()
  quick_sort_fast_example()
  print()
  merge_sort_example()
  

def bubble_sort_example():
  a = [int(x) for x in np.random.randint(low=1, high=128, size=100)]
  print("The random list of numbers: ")
  print(a)
  print("The sorted list of numbers with bubble sort: ")
  print(bubble_sort(a))

def bubble_sort_finish_early_example():
  a = [int(x) for x in np.random.randint(low=1, high=128, size=100)]
  print("The random list of numbers: ")
  print(a)
  print("The sorted list of numbers with bubble sort finish early: ")
  print(bubble_sort_finish_early(a))

def quick_sort_example():
  a = [int(x) for x in np.random.randint(low=1, high=128, size=100)]
  print("The random list of numbers: ")
  print(a)
  print("The sorted list of numbers with quick sort: ")
  print(quick_sort(a))

def quick_sort_fast_example():
  a = [int(x) for x in np.random.randint(low=1, high=128, size=100)]
  print("The random list of numbers: ")
  print(a)
  print("The sorted list of numbers with quick sort fast: ")
  print(quick_sort_fast(a))

def merge_sort_example():
  a = [int(x) for x in np.random.randint(low=1, high=128, size=100)]
  print("The random list of numbers: ")
  print(a)
  print("The sorted list of numbers with merge sort: ")
  print(merge_sort(a))

examples()
