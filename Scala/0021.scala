/**
 * Definition for singly-linked list.
 * class ListNode(_x: Int = 0, _next: ListNode = null) {
 *   var next: ListNode = _next
 *   var x: Int = _x
 * }
 */
object Solution {
    def mergeTwoLists(list1: ListNode, list2: ListNode): ListNode = {
        // Create a dummy node to simplify the merging process
        val dummy = new ListNode(0)
        var current = dummy
        
        // Initialize pointers for list1 and list2
        var l1 = list1
        var l2 = list2
        
        // Merge the two lists
        while (l1 != null && l2 != null) {
            if (l1.x <= l2.x) {
                current.next = l1
                l1 = l1.next
            } else {
                current.next = l2
                l2 = l2.next
            }
            current = current.next
        }
        
        // If there are remaining nodes in list1 or list2, append them
        if (l1 != null) {
            current.next = l1
        }
        if (l2 != null) {
            current.next = l2
        }
        
        // Return the merged list starting from the node after dummy
        dummy.next
    }
}