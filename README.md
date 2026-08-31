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
- Graphs comparing the tested performance of all the algorithms, and theoretical complexity

## Runtime

All of the algorithms were tested 10 times with the mean runtime recorded and plotted using Python's timeit module. This is then compared to the theoretical time complexity of each algorithm.

![Runtime](images/runtime_vs_input_size.png)

The above graph shows the mean runtime for lists of up to 5000 integers.

Individual speed tests for specific lengths of inputs, including lists of length 10,000, are able to be run separately.

## Complexity Analysis

| Algorithm | Best Case | Average Case | Worst Case |
|-----------|-----------|--------------|------------|
| Bubble Sort | O(n) | O(n²) | O(n²) |
| Quick Sort | O(n log n) | O(n log n) | O(n²) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) |

Using this, the graph below shows each of the runtimes divided by their respective average time complexity, e.g. Bubble Sort / $n^2$

![Runtime](images/normalised_runtime.png)

A horizontal line indicated that the results are consistent with their corresponding theoretical complexities. The bubble sort implementations do stray more noticably, potentially because larger input sizes are needed to show the long term growth.

## Usage

Individual algorithms can be run using the corresponding Python files.
