## Merge Sort vs Quick Sort vs Heap Sort
* time complexity: As already discussed in the other answers, the three algorithms are in average case O(nlogn) while quick sort worst case is O(n2).
* space complexity: especially if it's in-place sort Heap sort and quick sort can be done in-place. So they can directly work on the pre-allocated space where initial unsorted data is stored. While heap sort removes recursive calls by tail optimization and its space requirement is O(1), quick sort requires variables put on the stacks at each recursive step, so it requires in total O(logn) space. Merge sort is not in-place and requires additional O(n) space.
* external sort or not: This means whether the algorithm works efficiently with external memory (e.g. HDD/SSD) which is slower than the main memory. Merge sort and quick sort are typical external sort since they can divide target data set and work on the small pieces loaded on memory, but heap sort is difficult to do that.
* stable or unstable: Merge sort is only the stable sorting among the three.
* comparison based or not: Some algorithms such as Radix sort don't depend on comparison of two elements, though the three in questions are all comparison based.

