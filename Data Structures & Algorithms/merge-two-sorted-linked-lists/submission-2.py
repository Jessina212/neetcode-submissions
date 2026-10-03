# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p = list1
        q = list2
        c = 0

        if p == None and q == None:
            return p
        elif q == None:
            return p
        elif p == None:
            return q

        while p!=None and q!=None:
            if p.val > q.val:
                if c==0:
                    head3 = ListNode(q.val)
                    c = 1
                    t = head3
                else:
                    t.next = q
                    t = t.next
                q = q.next
            else:
                if c==0:
                    head3 = ListNode(p.val)
                    c = 1
                    t = head3
                else:
                    t.next = p
                    t = t.next
                p = p.next
        
        if p != None:
            while p!= None:
                if c==0:
                    head3 = ListNode(q.val)
                    c = 1
                    t = head3
                else:
                    t.next = p
                    t = t.next
                
                p = p.next

        elif q != None:
            while q != None:
                if c==0:
                    head3 = ListNode(q.val)
                    c = 1
                    t = head3
                else:
                    t.next = q
                    t = t.next
                
                q = q.next

        return head3