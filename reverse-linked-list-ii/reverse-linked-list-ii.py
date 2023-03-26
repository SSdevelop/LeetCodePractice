# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        # finding the first node of the range
        beforeRange, curr = dummy, head
        for i in range(left-1):
            beforeRange, curr = curr, curr.next
        
        # reversuing the links
        prev = None
        for i in range(right-left+1):
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        # resetting the links of nodes before and after the reversal
        beforeRange.next.next = curr
        beforeRange.next = prev

        return dummy.next
