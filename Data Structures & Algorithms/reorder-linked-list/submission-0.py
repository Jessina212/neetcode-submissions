# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        p = head
        c = 0
        d = {}
        while p != None:
            
            d[c] = p
            c += 1
            p = p.next
        
        h = head
        if c%2 != 0:
            for i in range(1, c//2 + 1):
                h.next = d[c - i]
                h = h.next
                h.next = d[i]
                h = h.next
        else:
            for i in range(1, c//2):
                h.next = d[c - i]
                h = h.next
                h.next = d[i]
                h = h.next
            h.next = d[c//2]
            h = h.next
        h.next = None