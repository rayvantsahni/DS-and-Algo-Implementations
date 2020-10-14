# =============================================================================
# Worst case complexity of this is O(N^2).
# But, in the case of Quick Sort we ususally consider the Average case, i.e O(N*log(N))
# Because the worst case scenario is very rare in these situation and can be avoided if the good pivot element is chosen
# =============================================================================

# =============================================================================
# In this algorithm, we use the divide and conquer approach.
# What we do is take 2 pointers, i.e one to iterate over the elements of the list,
# another to keep track of the partition position.
# Each element in the list is considered and compared with the pivot element
# and if it is greater than the pivot we do nothing and move to the next element.
# But in case when an element is smaller than or equal to the pivot, we swap 
# that element with the element at the partition pointer and then increment the partition
# pointer to point at the next element in line; this ensures that to the left of the
# partition pointer we have all elements lesser than or equal to the pivot.
# The partition is the point to the left of which all the elements are smaller than 
# or equal to the pivot.
# And hence, naturally all elements to the right would be greater than the pivot.
# This partition helps us to decide the perfect position of the pivot in this
# unsorted array, as it shoudl be placed right in between all elements smaller to it 
# all elements greater to it.
# So in other words we sandwich the pivot in between those 2 partitions and hence 
# we can claim that at the moment the pivot is in its right position in the list, 
# irrespective of the order of other elements.
# Then, we do this process all over again for the 2 partitions made by the pivot,
# i.e the lesser than pivot and greater than pivot partitions.
# =============================================================================

from random import randint, shuffle

def quick_sort(arr, start, end):
    if start >= end: #checking if the size of the array is 0 or 1
        return
    
    rand_index = randint(start, end) #picking out a random index to avoid worst case scenarios
    arr[end], arr[rand_index] = arr[rand_index], arr[end] #swapping the random index element with the one in last position
    pivot_index = end #storing the last index to be the index of the pivot
    
    i = start #pointer that keeps track of the boundary/partition which divides the array into 2 parts
    
    for j in range(start, end): #pointer which will iterate over each element to be compareed by the pivot
        if arr[j] <= arr[pivot_index]:
            arr[i], arr[j] = arr[j], arr[i] #swapping and taking the elemetn on the left if it is smaller than the pivot
            i += 1 #increasing the partition pointer
        
    arr[end], arr[i] = arr[i], arr[end] #swapping the partition pointer and the pivot, so that the pivot can be placed in its correct position
    
    quick_sort(arr, start, i - 1) #calling the quicksort function on the left half of the partition
    quick_sort(arr, i + 1, end) #calling the quicksort function on the right half of the partition
    
    return arr
    
    
    
def main():
    
    a = [randint(0, 50) for _ in range(10)]
    shuffle(a)
    print("Unsorted:", a, end = "\n\n")
    print("Sorted:", quick_sort(a, 0, len(a)-1), end = "\n\n")
    

main()
