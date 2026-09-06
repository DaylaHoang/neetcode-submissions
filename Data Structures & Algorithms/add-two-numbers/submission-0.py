# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Plan
        # 1. Start with carry = 0 and dummy node
        # 2. Add current digits from both lists + carry
        # 3. Store total % 10 in the result
        # 4. Set carry = total // 10
        # 5. Move both pointers forward
        # 6. Contunie while a list or carry remains
        # 7. Return dummy.next

        dummy = ListNode(0)
        current = dummy

        carry = 0
        while l1 or l2 or carry:
            digit1 = l1.val if l1 else 0
            digit2 = l2.val if l2 else 0
            total = digit1 + digit2 + carry
            
            current.next = ListNode(total % 10)
            carry = total // 10
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next