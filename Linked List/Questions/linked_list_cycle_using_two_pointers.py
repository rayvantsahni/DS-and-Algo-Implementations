# Definition for singly-linked list.
# class LinkedListNode:
#     def __init__(self, value = 0, next = None):
#         self.value = value
#         self.next = next

class Solution:
    def containsCycle(self, head):
        if not head or not head.next:
            return False
        
        slow = head
        fast = head.next
        
        while fast:
            if slow is fast:
                return True
            slow = slow.next
            try:
                fast = fast.next.next
            except:
                break
        
        return False
