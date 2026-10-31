# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dummy1 = head
        dummy2 = head

        while dummy2 and dummy2.next:
            dummy1 = dummy1.next
            dummy2 = dummy2.next.next
            if dummy1 == dummy2: 
                return True
        return False
