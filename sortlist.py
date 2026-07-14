class Solution(object):
    def sortList(self, head):
        if not head or not head.next:
            return head   
        prev = None
        slow = head
        fast = head  
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next     
        prev.next = None
        left_sorted = self.sortList(head)
        right_sorted = self.sortList(slow)
        return self.merge(left_sorted, right_sorted)
  
    def merge(self, list1, list2):
        dummy = ListNode(0)
        tail = dummy
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next 
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2    
        return dummy.next
