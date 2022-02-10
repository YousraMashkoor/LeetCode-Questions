# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        slow = head
        fast = head
        try:
            while(fast.next != None and fast !=None):
                slow = slow.next
                fast = fast.next.next

                if (fast == slow):
                    return True
            return False
        except:
            return False