class Solution(object):
    def reorderList(self, head):
        if not head or not head.next:
            return

        slow, fast = head, head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        curr = slow.next
        slow.next = None 
        prev = None
        
        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            
        first, second = head, prev
        while second is not None:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
