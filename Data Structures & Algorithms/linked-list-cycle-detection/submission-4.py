# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow=head
        if head:
            fast=head.next

            while fast!=None:
                slow=slow.next
                if fast.next==None:
                    break
                fast=fast.next.next
                if fast==slow:
                    return True
        return False
            

