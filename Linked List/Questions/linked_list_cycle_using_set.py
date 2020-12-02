# Definition for singly-linked list.
# class LinkedListNode:
#     def __init__(self, value = 0, next = None):
#         self.value = value
#         self.next = next

class Solution:
    def containsCycle(self, head):
        if not head or not head.next:
            return False
        
        current = head
        s = set()
        while current:
            if id(current) in s:
                return True
            s.add(id(current))
            current = current.next
        
        return False
