# Merge Sort vs Quick Sort vs Heap Sort
* time complexity: As already discussed in the other answers, the three algorithms are in average case O(nlogn) while quick sort worst case is O(n2).
* space complexity: especially if it's in-place sort Heap sort and quick sort can be done in-place. So they can directly work on the pre-allocated space where initial unsorted data is stored. While heap sort removes recursive calls by tail optimization and its space requirement is O(1), quick sort requires variables put on the stacks at each recursive step, so it requires in total O(logn) space. Merge sort is not in-place and requires additional O(n) space.
* external sort or not: This means whether the algorithm works efficiently with external memory (e.g. HDD/SSD) which is slower than the main memory. Merge sort and quick sort are typical external sort since they can divide target data set and work on the small pieces loaded on memory, but heap sort is difficult to do that.
* stable or unstable: Merge sort is only the stable sorting among the three.
* comparison based or not: Some algorithms such as Radix sort don't depend on comparison of two elements, though the three in questions are all comparison based.

### Comparing Quick and Heap Sorts
Empirical studies show that generally **quick sort is considerably faster than heapsort**.

The following counts of compare and exchange operations were made for three different sorting algorithms running on the same data:
![image](https://user-images.githubusercontent.com/38404580/89568693-4cbab600-d841-11ea-9296-ebcf0a3a17f6.png)

Thus, when an occasional "blowout" to `O(n^2)` is tolerable, we can expect that, **on average, quick sort will provide considerably better performance** - especially if one of the modified pivot choice procedures is used.

Most commercial applications would use quicksort for its better average performance: they can tolerate an occasional long run (which just means that a report takes slightly longer to produce on full moon days in leap years) in return for shorter runs most of the time.

However, **quick sort should never be used in applications which require a guarantee of response time**, unless it is treated as an `O(n^2)` algorithm in calculating the worst-case response time. If you have to assume `O(n^2)` time, then - if _n_ is small, you're better off using **insertion sort - which has simpler code and therefore smaller constant factors**.

And if _n_ is large, you should obviously be using **heap sort**, for its guaranteed `O(n.log(n))` time. Life-critical (medical monitoring, life support in aircraft and space craft) and mission-critical (monitoring and control in industrial and research plants handling dangerous materials, control for aircraft, defence, etc) software will generally have a response time as part of the system specifications. In all such systems, it is not acceptable to design based on average performance, you must always allow for the worst case, and thus treat quicksort as `O(n^2)`.
