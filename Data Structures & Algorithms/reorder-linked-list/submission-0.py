# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Plan
        # 1. Find the middle using slow/fast pointers
        # 2. Split the list into two halves
        # 3. Reverse the second half
        # 4. Merge the two halves by alternativing nodes

        if not head or not head.next:
            return

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None
        previous = None

        while second:
            next_node = second.next
            second.next = previous
            previous = second
            second = next_node
        second = previous

        first = head
        while second:
            first_next = first.next
            second_next = second.next
            first.next = second
            second.next = first_next

            first = first_next
            second = second_next

