# =============================================================================
# Insertion Sort is Stable.
# Complexity is O(N^2).
# =============================================================================

def insertion_sort(arr):
    for i in range(1, len(arr)):
        
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1

    return arr

    
def main():
    from random import randint, shuffle
    
    a = [randint(0, 50) for _ in range(10)]
    shuffle(a)
    print("Unsorted:", a, end = "\n\n")
    print("Sorted:", insertion_sort(a), end = "\n\n")
    

main()
