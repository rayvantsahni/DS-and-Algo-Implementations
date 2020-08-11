# =============================================================================
# Complexity of Bubble sort is originally O((N)*(N-1)) i.e O(N^2)
# Although it can be reduced to O((N)*(N-1)/2),
# but still the order does not change from O(N^2).
# =============================================================================

def bubble_sort(arr):
    
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
              
    return arr

    
    
def main():
    from random import randint, shuffle
    
    a = [randint(0, 50) for _ in range(10)]
    shuffle(a)
    print("Unsorted:", a, end = "\n\n")
    print("Sorted:", bubble_sort(a), end = "\n\n")
    
main()
