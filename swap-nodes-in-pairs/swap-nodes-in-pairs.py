# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        dummy = ListNode(next=head)
        prev, curr = dummy, head

        while curr and curr.next:
            # storing the values
            nxtPair = curr.next.next
            second = curr.next
            #swapping
            second.next = curr
            curr.next = nxtPair
            prev.next = second
            #shifting
            prev = curr
            curr = nxtPair
        
        return dummy.next