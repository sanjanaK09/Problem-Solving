# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        for _ in range(k):
            if not curr:
                return head
            curr = curr.next
            
        prev, node = None, head
        for _ in range(k):
            nxt = node.next
            node.next = prev
            prev = node
            node = nxt
            
        head.next = self.reverseKGroup(node, k)
        return prev
        