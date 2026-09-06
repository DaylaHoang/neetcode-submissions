# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Plan
        # 1. Put a dummy node before head
        # 2. Move fast n steps ahead
        # 3. move fast and slow together until fast reaches the end
        # 4. slow is right before the node to remove
        # 5. skip slow.next
        # 6. Return dummy.next

        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0:
            right = right.next
            n -= 1
        while right:
            left = left.next
            right = right.next
        left.next = left.next.next
        return dummy.next


