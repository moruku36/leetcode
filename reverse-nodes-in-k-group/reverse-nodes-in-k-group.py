# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        
        pre = dummy
        cur = head
        
        i = 0
        while cur:
            i += 1
            if i % k == 0:
                pre = self.reverseOneGroup(pre, cur.next)
                cur = pre.next
            else:
                cur = cur.next
        
        return dummy.next
    
    def reverseOneGroup(self, pre, nxt):
        last = pre.next
        cur = last.next
        
        while cur != nxt:
            last.next = cur.next
            cur.next = pre.next
            pre.next = cur
            
            cur = last.next
        
        return last