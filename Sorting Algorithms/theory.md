# Sorting Algorithms

- ### Bubble Sort:
Bubble sort is an algorithm to sort a list through repeated swaps of adjacent elements. It has a runtime of `O(N^2)`.

- ### Merge Sort:
Merge Sort has the best, worst, and average time complexity all the same as `Θ(N*log(N))`. Merge sort also requires space. Each separation requires a temporary array, and so a merge sort would require enough space to save the whole of the input a second time. This means the worst-case space complexity of merge sort is `O(N)`.

- ### Quick Sort:
Quicksort is an efficient recursive algorithm for sorting arrays or lists of values. The algorithm is a _comparison_ sort, where values are ordered by a comparison operation such as **>** or **<**. Quicksort is an unusual algorithm in that the worst case runtime is `O(N^2)`, but the average case is `O(N*log(N))`.

- ### Radix Sort:
_A radix is the base of a number system. For the decimal number system, the radix is 10_.
The most amazing feature of radix sort is that it manages to sort a list of integers without performing any comparisons whatsoever. We call this a non-comparison sort. The complexity of radix sort is `O(wn)` where, **w is the average number of digits or the _word-size_**. Assuming the length of the list is much larger than the number of digits, we can consider **w a constant factor** and this can be reduced to `O(n)`.


#### For some great visualization of the sorting algortithms, click [here](https://www.toptal.com/developers/sorting-algorithms).
