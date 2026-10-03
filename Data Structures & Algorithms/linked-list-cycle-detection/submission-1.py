# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        p = head
        if p == None:
            return False
        c = 0
        d = {}
        while p!=None:
            if p.next == None:
                return False
            elif p not in d:
                d[p] = 'visited'
                p = p.next
            elif p in d:
                return True