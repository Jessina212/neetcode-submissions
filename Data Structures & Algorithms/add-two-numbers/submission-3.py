# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # p = l1
        # q = l2
        # sum = 0
        # head3 = ListNode()
        # c = 0

        # while p!=None and q!=None:
        #     sum = p.val + q.val
            
        #     if c==0:
        #         if sum > 9:
        #             a = sum%10
        #             b = sum//10
        #             head3.val = a
        #             t = head3
        #             t.next = ListNode()
        #             t.next.val = b
        #             t = t.next
        #         else:
        #             head3.val = sum
        #             t = head3
        #         c = 1
        #     else:
        #         t.next = ListNode()
        #         t.next.val = sum
        #         t = t.next
        #     p = p.next
        #     q = q.next
        # if p!= None:
        #     while p!= None:
        #         t.next = ListNode()
        #         t.next.val = p.val
        #         t = t.next
        #         p = p.next
        # if q!= None:
        #     while q!=None:
        #         t.next = ListNode()
        #         t.next.val = q.val
        #         t = t.next
        #         q = q.next
        
        # return head3
        
        p = l1
        q = l2
        c = 1
        num1 = 0
        while p!=None:
            num1+=(p.val*c)
            c*=10
            p = p.next
        num2 = 0
        c = 1
        while q!=None:
            num2+=(q.val*c)
            c*=10
            q = q.next
        
        sum = num1+num2
        sum = str(sum)
        sum = list(sum)
        sum = sum[::-1]
        
        head3 = ListNode(sum[0])
        t = head3
        for i in range(1, len(sum)):
            t.next = ListNode(sum[i])
            t = t.next
        
        return head3
