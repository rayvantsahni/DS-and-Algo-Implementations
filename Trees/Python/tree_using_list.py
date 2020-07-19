# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 20:11:41 2020

@author: Rayvant Sahni
"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []
    
    def add_child(self, child_node):
        print("\nAdding", child_node.value, "as a child for", self.value, end = "\n")
        self.children.insert(0, child_node)
        
    def remove_child(self, child_node):
        print("\nRemoving child", child_node.value, "from", self.value, end = "\n")
        self.children.remove(child_node)
        
    def traverse(self):
        nodes_to_visit = [self]
        while len(nodes_to_visit):
            current_node = nodes_to_visit.pop()
            print(current_node.value, end = "  ")
            nodes_to_visit.extend(current_node.children)
            
root = TreeNode("root")

child_a = TreeNode("A")
child_b = TreeNode("B")
child_c = TreeNode("C")
child_d = TreeNode("D")
child_e = TreeNode("E")
child_f = TreeNode("F")
child_g = TreeNode("G")

root.add_child(child_a)
root.add_child(child_b)
root.add_child(child_c)

child_a.add_child(child_d)
child_a.add_child(child_e)

child_c.add_child(child_f)

child_f.add_child(child_g)
root.traverse()

child_f.remove_child(child_g)
root.traverse()

root.remove_child(child_b)
root.traverse()

'''
    ROOT
   / | \
  a  b  c
 / \     \
d   e     f
          |
          g
'''
