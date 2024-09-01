class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        
        # Step 1: Find the middle of the list
        mid = self.findMiddle(head)
        second_half = mid.next
        mid.next = None  # Split the list into two halves
        
        # Step 2: Reverse the second half of the list
        second_half = self.reverseList(second_half)
        
        # Step 3: Merge the two halves
        self.mergeLists(head, second_half)

    def findMiddle(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

    def mergeLists(self, l1, l2):
        while l1 and l2:
            temp1 = l1.next
            temp2 = l2.next
            
            l1.next = l2
            l1 = temp1
            
            l2.next = l1
            l2 = temp2
