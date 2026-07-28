class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        fast = dummy
        slow = dummy
        
        for _ in xrange(n + 1):
            fast = fast.next
            
        while fast is not None:
            fast = fast.next
            slow = slow.next
            
        slow.next = slow.next.next
        return dummy.next
