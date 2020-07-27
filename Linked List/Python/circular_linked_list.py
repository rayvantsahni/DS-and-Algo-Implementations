# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 19:33:20 2020

@author: Rayvant Sahni
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
    def get_value(self):
        return self.value
    
    def get_next(self):
        return self.next
    
    
    
    
class CircularLinkedList:
    def __init__(self, head = None):
        self.head = head
        
    
    def prepend(self, new_value):
        new_node = Node(new_value)
        
        if not self.head:
            self.head = new_node
            self.head.next = new_node
            return
        else:
            new_node.next = self.head            
            current_node = self.head
            while current_node.get_next() != self.head:
                current_node = current_node.get_next()
            current_node.next = new_node
            self.head = new_node
            return
        
        
    def append(self, new_value):
        new_node = Node(new_value)
        
        if not self.head:
            self.head = new_node
            self.head.next = new_node
            return
        else:
            new_node.next = self.head
            current_node = self.head
            while current_node.get_next() != self.head:
                current_node = current_node.get_next()
            current_node.next = new_node
            
            
    def exists(self, value_to_find):
        if not self.head:
            return False
        else:
            if self.head.get_value() == value_to_find:
                return True
            current_node = self.head.get_next()
            while current_node.get_value() != value_to_find:
                current_node = current_node.get_next()
                if current_node == self.head:
                    return False
            return True
            
        
    def remove(self, value_to_remove):
        if not self.head:
            print("List is already empty.")
            return
        elif not self.exists(value_to_remove):
            print(value_to_remove, "not in list.")
            return
        elif self.head.get_value() == value_to_remove and self.head.get_next() == self.head:
            self.head.next = None
            self.head = None
            return
        elif self.head.get_value() == value_to_remove:
            current_node = self.head
            while current_node.get_next() != self.head:
                current_node = current_node.get_next()
            current_node.next = self.head.get_next()
            self.head = self.head.get_next()
            return
        else:
            current_node = self.head
            while current_node.get_next().get_value() != value_to_remove:
                current_node = current_node.get_next()
            current_node.next = current_node.get_next().get_next()
            return
        
        
    def length(self):
        if not self.head:
            return 0
        else:
            count = 0
            current_node = self.head
            while current_node.get_next() != self.head:
                count += 1
                current_node = current_node.get_next()
            return count + 1


    def print_list(self):
        if not self.head:
            print("List is empty.")
            return
        else:
            print('-' * 12)
            print("LINKED LIST")
            print('-' * 12)
            current_node = self.head
            while current_node:
                print(current_node.get_value())
                current_node = current_node.get_next()
                if current_node == self.head:
                    break
        
            
            
            
            
c = CircularLinkedList()

c.prepend(40)
c.prepend(50)
c.prepend(60)
c.prepend(70)
c.prepend(80)
c.append(-5)
c.append(-4)
c.append(-3)
c.append(-2)
c.append(-1)

c.print_list()
print("LENGTH:", c.length())

c.remove(40)
c.remove(-1)
c.remove(-5)

print("\nAfter Removal...")
c.print_list()
print("LENGTH:", c.length())

            

            
