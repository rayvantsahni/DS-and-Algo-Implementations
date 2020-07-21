# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 00:18:48 2020

@author: Rayvant Sahni
"""

class MinHeap:
    def __init__(self):
        self.heap_list = [None] #stores the elements of the heap in the form of a list
        self.element_count = 0 #stores the number of elements
        
    def __repr__(self): #to print/show the elements of the heap list when we print the object of the MinHeap class
        return "\nHeap List - " + str(self.heap_list)
        
    def get_parent_index(self, index): #gives the index of the parent of an element in the list,i.e floor(index of child / 2)
        return index // 2
    
    def get_left_child_index(self, index): #gives the index of the left child of an element in the list, i.e (index of parent * 2)
        return index * 2
    
    def get_right_child_index(self, index): #gives the index of the right child of an element in the list, i.e (index of parent * 2) + 1
        return index * 2 + 1
    
    def child_exists(self, index): #checks if a particular element has a child as of yet
        return self.get_left_child_index(index) <= self.element_count
        
    
    def add(self, element): #to add an element to the heap
        print("\nAdding", element, "to", self.heap_list)
        self.element_count += 1
        self.heap_list.append(element)
        self.heapify_up()
        
        
    def heapify_up(self): #comes into action when an element is added to the heap; checks if any parent has a value greater than the child
        print("HEAPIFYING UP..")
        index = self.element_count #makes the index to start with, equal to the index of the last element in the heap list
        flag = False #using a flag variable to ensure the loop breaks as soon as the parent is smaller than the child, i.e no more swaps required
        while self.get_parent_index(index) > 0: #loop runs only till the element can have a parent, i.e it parent cannot go higher than the root/first element in the list
            if flag: #this breaks the loop if the program enters the 'else' condition, i.e no more swaps required
                break #breaks the while loop
            if self.heap_list[self.get_parent_index(index)] > self.heap_list[index]: #if the parent is greater than the child, then the elements are swapped
                # print("Swapping-\n", " Parent:", self.heap_list[self.get_parent_index(index)], "and Child:", self.heap_list[index], end = "\n")
                self.heap_list[self.get_parent_index(index)], self.heap_list[index] = self.heap_list[index], self.heap_list[self.get_parent_index(index)] #swapping the elements of the parent and the child
            else:
                flag = True #changes the flag to True so that the loop can be broken
            index = self.get_parent_index(index) #replacing the old index, i.e the index with which we started, with the new one, i.e the index of the parent of the original position of the element
        print("Heap property restored:", self.heap_list)
            
             
    def heapify_down(self): #comes into action when the minimum element is removed from the heap; checks if any child has a value less than the parent
        index = 1 #makes the index to start with, equal to the index of the first element in the heap list
        
        while self.child_exists(index): #loop runs only till the element has children
            print("HEAPIFYING DOWN..")
            smaller_child_index = self.get_smaller_child_index(index) #selecting the child which contains a smaller value
            
            if self.heap_list[index] > self.heap_list[smaller_child_index]: #if the child is less than the parent, then the elements are swapped
                self.heap_list[index], self.heap_list[smaller_child_index] = self.heap_list[smaller_child_index], self.heap_list[index] #swapping the elements of the child and the parent
            index = smaller_child_index
        print("Heap property restored:", self.heap_list)
            
            
    def get_smaller_child_index(self, index): #returns the child which contains a smaller value
        if self.get_right_child_index(index) > self.element_count: #checks if the right child exists or not
            print("Only left child exists")
            return self.get_left_child_index(index)
        else:
            left_child_value = self.heap_list[self.get_left_child_index(index)]
            right_child_value = self.heap_list[self.get_right_child_index(index)]
            if left_child_value < right_child_value:
                print("<left child is smaller>")
                return self.get_left_child_index(index)
            else:
                print("<right child is smaller>")
                return self.get_right_child_index(index)
        
            
    def retrieve_min(self): #removes the minimum value of the heap, i.e the value present at the root
        if self.element_count == 0: #checking if the root is empty or not
            print("Heap is Empty.")
            return
        
        min = self.heap_list[1]
        print("\nRemoving", min, "from", self.heap_list)
        self.heap_list[1], self.heap_list[-1] = self.heap_list[-1], self.heap_list[1] #swapping the last added element of the heap list with the first element/root
        self.heap_list.pop() #removing the minimum value from the heap list
        self.element_count -= 1
        print("Last element moved to first:", self.heap_list)
        self.heapify_down()
        return



heap = MinHeap()
print(heap)

heap.add(100)
heap.add(120)
heap.add(30)
heap.add(80)
heap.add(200)
heap.add(90)
heap.add(70)
heap.add(150)
heap.add(50)
heap.add(170)
heap.add(130)
heap.add(10)

heap.retrieve_min()
heap.retrieve_min()
heap.retrieve_min()
heap.retrieve_min()

print(heap)
    
    
    
    
    
    
    
    
    
    
    
    
    
