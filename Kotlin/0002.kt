/**
 * Example:
 * var li = ListNode(5)
 * var v = li.`val`
 * Definition for singly-linked list.
 * class ListNode(var `val`: Int) {
 *     var next: ListNode? = null
 * }
 */
class Solution {
    fun addTwoNumbers(l1: ListNode?, l2: ListNode?): ListNode? {
        // Create a dummy node to simplify operations
        val dummyHead = ListNode(0)
        var current = dummyHead
        var carry = 0

        var p = l1
        var q = l2

        // Traverse both linked lists
        while (p != null || q != null || carry != 0) {
            // Get the current values
            val x = p?.`val` ?: 0
            val y = q?.`val` ?: 0

            // Calculate the sum of current digits and carry
            val sum = x + y + carry
            carry = sum / 10
            val newVal = sum % 10

            // Create a new node with the computed value
            current.next = ListNode(newVal)
            current = current.next!!

            // Move to the next nodes in the lists
            p = p?.next
            q = q?.next
        }

        // Return the next of dummy node, which is the head of the result list
        return dummyHead.next
    }
}