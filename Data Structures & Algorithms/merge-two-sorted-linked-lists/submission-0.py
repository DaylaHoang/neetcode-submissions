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
        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                current = list1
                list1 = list1.next
            else:
                current.next = list2
                current = list2
                list2 = list2.next
        current.next = list1 if list1 else list2
        return dummy.next





