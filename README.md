# Sorting-Algorithms

A Python project implementing and comparing the performance of multiple sorting algorithms.

## Features
- Two bubble sort algorithms
- Two quick sort algorithms
- One merge sort algorithm
- One insertion sort algorithm
- A speed test between the bubble sorts
- A speed test between the quick sorts
- Examples of all the sorting algorithms working
- Speed test for lists of lengths: 100, 1000, 10000 between all of the algorithms
- Graphs outlining the speed of all the algorithms, and performance realtive to theory

## Runtime

All of the algorithms were tested 10 times with the mean runtime recorded and plotted using Python's timeit module. This is then compared to the theortical time complexity of each algorithm.

![Runtime](images/runtime_vs_input_size.png)

The above graph shows the  mean runtime for lists of up to 5000 integers.

## Complexity Analysis

| Algorithm | Best Case | Average Case | Worst Case |
|-----------|-----------|--------------|------------|
| Bubble Sort | O(n) | O(n²) | O(n²) |
| Quick Sort | O(n log n) | O(n log n) | O(n²) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) |

Using this, the below graph is each of the runtimes divided by there respective average time complexity, e.g. Bubble Sort / $n^2$

![Runtime](images/normalised_runtime.png)

When the line is straight that shows that the results are in line with the theoretical values, so all bar the bubble sorts are as expected. The bubble sorts may need longer to reach a constant due to the slower nature of bubble sort.

## Usage

Individual algorithms can be run using the corresponding Python files.
