
// Definition for singly-linked list.
class ListNode {
  int val;
  ListNode? next;
  ListNode([this.val = 0, this.next]);
}

class Solution {
  ListNode? addTwoNumbers(ListNode? l1, ListNode? l2) {
    // Initialize a dummy node to build the result list
    ListNode dummyHead = ListNode(0);
    ListNode current = dummyHead;
    int carry = 0;

    // Traverse both lists
    while (l1 != null || l2 != null || carry > 0) {
      // Get the values from the nodes if available
      int val1 = (l1 != null) ? l1.val : 0;
      int val2 = (l2 != null) ? l2.val : 0;
      
      // Compute the sum of values and carry
      int sum = val1 + val2 + carry;
      carry = sum ~/ 10; // Update carry for the next digit
      int digit = sum % 10; // Current digit to store in the node

      // Create a new node with the computed digit
      current.next = ListNode(digit);
      current = current.next!; // Move to the next node

      // Move to the next nodes in l1 and l2 if available
      if (l1 != null) l1 = l1.next;
      if (l2 != null) l2 = l2.next;
    }

    // Return the next of dummyHead which points to the head of the result list
    return dummyHead.next;
  }
}