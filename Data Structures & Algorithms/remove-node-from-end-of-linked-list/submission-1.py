# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        dummy = head
        while dummy:
            count += 1
            dummy = dummy.next
        
        remove_at = count - n
        curr = head
        if remove_at == 0: return curr.next
        for i in range(count):
            if i == remove_at - 1:
                curr.next = curr.next.next
                break
            curr = curr.next
        return head
