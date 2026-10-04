# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # if n == 1:
        #     p = head
        #     if p == None or p.next == None:
        #         return p

        #     while p.next.next != None:
        #         p = p.next
            
        #     p.next = None

        #     return head
        
        # else:
        #     return self.removeNthFromEnd(head, n-1)

        p = head
        c = 0
        while p!= None:
            c += 1
            p = p.next
        
        if c == n:
            return head.next
        n = c - n + 1
        t = 0

        p = head
        while p!=None:
            t += 1
            if t+1 == n:
                p.next = p.next.next
                return head
            p = p.next
        return head