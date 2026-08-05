# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow=head
        fast=head
        prev=None
        nxt=None
        
        while fast!=None:
            
            if fast.next==None:
                break
            slow=slow.next
            fast=fast.next.next
        curr=slow.next
        slow.next=None
        while curr!=None:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt

        h=head

        while prev!=None:
            h_nxt=h.next
            h.next=prev
            p_nxt=prev.next
            prev.next=h_nxt
            prev=p_nxt
            h=h_nxt
        






        

         


