# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        cur = head
        sum = 0
        while l1 or l2:
            if l1:#l1 don't empty 
                sum += l1.val# accumulates the sum of two node values 
                l1 = l1.next# the refresh node 
            if l2:
                sum += l2.val# accumulates the sum of two node values 
                l2 = l2.next# the refresh node 
            cur.next = ListNode(sum % 10) # refresh the new list 
            cur = cur.next
            sum = sum // 10
        if sum != 0:
            cur.next = ListNode(sum)
        return head.next