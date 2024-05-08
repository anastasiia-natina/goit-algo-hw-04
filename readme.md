  Sorting Algorithms Comparison and Merge k Sorted Lists
This Python script compares three sorting algorithms: merge sort, insertion sort, and Timsort, in terms of their execution time. Additionally, it includes a function to merge k sorted lists into one sorted list.

  Description
The script contains implementations of the following algorithms:

  Merge_sort: A divide-and-conquer algorithm that recursively divides the input array into halves, sorts them, and then merges them.
  Insertion_sort: An algorithm that builds the final sorted array one element at a time by repeatedly taking the next element and inserting it into the proper position in the already sorted part of the array.
  Timsort: A hybrid sorting algorithm derived from merge sort and insertion sort, used as the default sorting algorithm in Python.
Usage
Ensure you have Python installed on your system.
Run the script sorting_algorithms.py.
The script will generate random data for testing purposes and measure the execution time of each sorting algorithm.
The comparison results will be printed to the console.
Functionality
The script compares the execution time of merge sort, insertion sort, and Timsort on randomly generated data. It uses the timeit module to measure the time taken by each algorithm.

Additionally, the script includes a function merge_k_lists that merges k sorted lists into one sorted list. This function can be used to merge multiple sorted arrays efficiently.

Files
sorting_algorithms.py: The main Python script containing implementations of sorting algorithms and the merge_k_lists function.
README.md: This readme file providing an overview of the script and instructions for usage.
Requirements
Python 3.x
Credits
This script was created by [Anastasiia].

License
This project is licensed under the MIT License - see the LICENSE file for details.