# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        tail = head
        length = 1
        while tail.next:
            tail = tail.next
            length += 1
            
        k = k % length
        if k == 0:
            return head
            
        tail.next = head
        for _ in range(length - k):
            tail = tail.next
            
        new_head = tail.next
        tail.next = None
        return new_head
      