/**
 * Definition for singly-linked list.
 * class ListNode(_x: Int = 0, _next: ListNode = null) {
 *   var next: ListNode = _next
 *   var x: Int = _x
 * }
 */
object Solution {
    def removeNthFromEnd(head: ListNode, n: Int): ListNode = {
        // Create a dummy node which helps in edge cases like removing the head
        val dummy = new ListNode(0)
        dummy.next = head
        
        // Initialize the two pointers
        var first: ListNode = dummy
        var second: ListNode = dummy
        
        // Move `first` pointer n+1 steps ahead
        for (_ <- 0 to n) {
            first = first.next
        }
        
        // Move both pointers until `first` reaches the end
        while (first != null) {
            first = first.next
            second = second.next
        }
        
        // `second.next` is the node to be removed
        second.next = second.next.next
        
        // Return the new head which is the next of dummy
        dummy.next
    }
}