def selection_sort(arr):
    for sorted_till in range(len(arr)-1): #keeps track of the position before which all elements are sorted
        min_index = sorted_till #taking the first element in the unsorted part as the index with the minimum value
        
        for i in range(sorted_till+1, len(arr)): #iterating from the 2nd value in the unsorted part till the end of the list
            if arr[i] < arr[min_index]: #comparing at each step to get the index carrying the minimum value
                min_index = i #assigning a minimum value index
            
        arr[sorted_till], arr[min_index] = arr[min_index], arr[sorted_till] #placing the minimum value found in the unsorted part of the list to the end of of the sorted part
    return arr
    

def main():
    from random import randint, shuffle
    
    a = [randint(0, 50) for _ in range(10)]
    shuffle(a)
    print("Unsorted:", a, end = "\n\n")
    print("Sorted:", selection_sort(a), end = "\n\n")
    

main()
