# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# PLAN
# 1. Create a dummy node and point current to it
# 2. Compare the current nodes of list1 and list2
# 3. Attach the smaller node to current
# 4. Move that list's pointer forward
# 5. Move current forward
# 6. Attach whichever list remains
# 7. Return dummy.next.


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # I use a dummy node so I don't need special logic for
        # choosing the head of the merged list.
        #
        # The real merged list will start at dummy.next.
        dummy = ListNode()

        # "current" always points to the last node in our merged list.
        # Initially, that's the dummy node.
        current = dummy

        # Continue while BOTH lists still have nodes to compare.
        while list1 and list2:

            # Since both lists are sorted, the smaller current value
            # must be the next node in the merged sorted list.
            if list1.val <= list2.val:

                # Reuse the existing node from list1.
                # We are changing pointers, not creating a new data node.
                current.next = list1

                # Move list1 forward because we just used its current node.
                list1 = list1.next

            else:
                # list2 has the smaller value, so reuse its current node.
                current.next = list2

                # Move list2 forward because we just used its current node.
                list2 = list2.next

            # Move current forward to the node we just attached.
            # This maintains the invariant that everything before current
            # is already correctly merged and sorted.
            current = current.next

        # At this point, at least one list is empty.
        #
        # The remaining list is already sorted, and every remaining value
        # is >= the values we've already placed, so we can attach it directly.
        if list1:
            current.next = list1
        else:
            current.next = list2

        # dummy itself is not part of the answer.
        # The actual head of the merged list is dummy.next.
        return dummy.next





