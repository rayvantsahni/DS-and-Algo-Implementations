# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 14:22:35 2020

@author: Rayvant Sahni
"""

def heapify(arr, n, root):
    maximum = root #assuming the root has the maximum value in this heap as of now
    left = 2 * root + 1 #defining the left child index of the root node
    right = 2 * root + 2 #defining the right child index of the root node
    
    if left < n: #checking if this parent has a left child(this also checks if the parent has any child whatsoever, as the minimum requirements to have children is to have atleast a left child)
        if arr[left] > arr[maximum]: #checking if the left child has a value greater than the root
            maximum = left #assigning the left child as the maximum value
        if right < n and arr[right] > arr[maximum]: #checking if the right child exists and also has a value greater than the maximum value till now
            maximum = right #assigning the right child as the maximum value
            
        if maximum != root: #checking if the maximum value has changed from the root(as assigned originally)
            arr[maximum], arr[root] = arr[root], arr[maximum] #swapping the root with the new maximum value to restore heap properties
            heapify(arr, n, maximum) #heapifying to restore the potential lose of the heap properties in the heap whose root is the node that was swapped by its parent
        
def heap_sort(arr):
    for nodes in range(len(arr)//2 - 1, -1, -1): #iterating over all nodes in a bottom up approach; starting from 'len(arr)//2 - 1' as that would be the first non leaf node in complete binary tree and all leafe nodes are already max heaps
        heapify(arr, len(arr), nodes) #heapifying them to convert the heap and its sub-heaps to max heaps
    
    for index in range(len(arr)-1, 0, -1): #iterating over elements to remove the root node(i.e node having the maximum value)
        arr[index], arr[0] = arr[0], arr[index] #swapping the root node with the last node
        heapify(arr, index, 0) #heapifying to restore the heap property after swapping of the nodes
        
    return arr


def main():
    from random import randint, shuffle
    
    a = [randint(0, 50) for _ in range(10)]
    shuffle(a)
    print("Unsorted:", a, end = "\n")
    print("\nSorted:", heap_sort(a), end = "\n")
    

main()





