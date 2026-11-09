# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head: return []

        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        remove_at = length - n
        if remove_at == 0: return head.next

        curr2 = head
        for i in range(length - 1):
            if i == remove_at - 1:
                curr2.next = curr2.next.next
            curr2 = curr2.next
        return head
                

