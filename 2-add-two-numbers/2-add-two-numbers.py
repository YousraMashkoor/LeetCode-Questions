# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        fake = p = ListNode(0)
        p1 = l1; p2 = l2
        carry = 0

        while(p1 or p2 or carry):
            
            sum = carry
            if p1: sum += p1.val; p1 = p1.next 
            if p2: sum += p2.val; p2 = p2.next

            carry = sum // 10
            unitsSum = sum % 10

            p.next = ListNode(unitsSum)

            p = p.next

        return fake.next