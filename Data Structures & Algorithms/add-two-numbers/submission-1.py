# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=node=ListNode(0)
        p1=l1
        p2=l2
        carry=0
        while p1 or p2 or carry:
            if p1 :
                v1=p1.val
            else:
                v1=0
            if p2:
                v2=p2.val
            else:
                v2=0
            
            sum=v1+v2+carry

            carry=sum//10
            new_val=sum%10
            node.next=ListNode(new_val)
            node=node.next
            if p1:
               p1=p1.next
            if p2:
               p2=p2.next        
        
        return dummy.next
            
