# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev=None
        curr=head
        nxt=None
        cu=head
        l=0
        while cu:
           l+=1
           cu=cu.next
        if l==1:
            head=None
            return head
               
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        head=prev
        past=None
        pre=prev
        fut=None
        while pre and n!=0:
            n-=1
            fut=pre.next
            if n==0:
                if past:
                    past.next=fut
                else:
                    head=fut
                continue
            past=pre
            pre=pre.next

        pr=None
        cur=head
        nx=None

        while cur:
            nx=cur.next
            cur.next=pr
            pr=cur
            cur=nx
        head=pr

        return head

        



            
            