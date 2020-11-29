# Definition for singly-linked list.
# class LinkedListNode:
#     def __init__(self, value = 0, next = None):
#         self.value = value
#         self.next = next


class Solution:
    def reverseList(self, head):  # Reversing the linked list in place i.e, O(1) space
        if not head or not head.next:  # if the linked list is empty or contains only one node, simply return the head node
            return head

        current_node = head  # keeps track of the current node we are on
        next_node = head  # holds the next node we'll go to before we change the pointer of the current node's next node to previos node
        previous_node = None  # holds the previous node where the current node's next pointer will point after it's direction is reversed

        while current_node:  
            next_node = current_node.next  # holding the next node to go to, before reversing the direction of the current node's next node
            current_node.next = previous_node  # reversing the pointer of the current node's next node to point to the previous node
            previous_node = current_node 
            current_node = next_node  # going forward to the next node to reverse its next pointer

        # by this point the 'current_node' and 'next_node' pointers have traversed the whole list and now point to None, whereas 'previous_node' pointer still points to the first node of the newly reversed list, hence it is made the head of the list
        head = previous_node
        return head
