# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy1 = head
        count = 0
        while dummy1:
            count += 1
            dummy1 = dummy1.next

        remove = count - n
        if remove == 0:
            return head.next
        
        dummy2 = head
        for i in range(count - 1):
            if i + 1 == remove:
                dummy2.next = dummy2.next.next
                break
            dummy2 = dummy2.next
        return head
