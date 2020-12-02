# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

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
