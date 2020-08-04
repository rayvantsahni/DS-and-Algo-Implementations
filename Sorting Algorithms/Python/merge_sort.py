# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 21:10:08 2020

@author: Rayvant Sahni
"""

# =============================================================================
# Complexity if Merge sort is O(N*log(N)).
# Space Complexity is O(N).
# Merge Sort is Stable.
# =============================================================================

def merge_sort(arr):
    if len(arr) <= 1: #checks if the arrays have been broken down to a single element or less
        return arr #this is where we stop dividing further and start merging it up
    
    middle_index = len(arr) // 2 #finding the middle index to split on
    
    left = merge_sort(arr[:middle_index]) #splitting the left split further
    right = merge_sort(arr[middle_index:]) #splitting the right split further
    
    return merge(left, right) #merging the left and right splits


def merge(left, right):
    merge_arr = [] #this will hold the merged splits
    
    while left and right: #looping until one of the splits are out of elements
        if left[-1] < right[0]: #handling the case where the list is already sorted and doesn't really require comparisons among each element of the 2 sublists
            merge_arr.extend(left) #if the last element of the left list is already greater than the first element of the right, we merge then without any further comparisons
            left.clear() #emptying the left list
            break
        elif left[0] <= right [0]:
            merge_arr.append(left.pop(0)) #removing from the left split and adding in the merge array
        else:
            merge_arr.append(right.pop(0)) #removing from the right split and adding in the merge array
        
    if left: #checking if left is still not empty
        merge_arr.extend(left) #adding all the remaining elements in the left split as it is as they are already sorted
    else:
        merge_arr.extend(right) #adding all the remaining elements in the right split as it is as they are already sorted
        
    return merge_arr #returning the array which holds the merged splits
            


def main():
    from random import randint, shuffle
    
    a = [randint(0, 200) for _ in range(20)]
    shuffle(a)
    print("Unsorted:", a, end = "\n\n")
    print("Sorted:", merge_sort(a), end = "\n\n")
    

main()
