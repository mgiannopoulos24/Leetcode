/**
 * Definition for a singly-linked list.
 * class ListNode {
 *     public $val = 0;
 *     public $next = null;
 *     function __construct($val = 0, $next = null) {
 *         $this->val = $val;
 *         $this->next = $next;
 *     }
 * }
 */
class Solution {

    /**
     * @param ListNode $l1
     * @param ListNode $l2
     * @return ListNode
     */
    function addTwoNumbers($l1, $l2) {
        // Create a dummy node to simplify operations
        $dummyHead = new ListNode(0);
        $current = $dummyHead;
        $carry = 0;

        // Traverse both linked lists
        while ($l1 !== null || $l2 !== null || $carry !== 0) {
            // Get the current values
            $val1 = ($l1 !== null) ? $l1->val : 0;
            $val2 = ($l2 !== null) ? $l2->val : 0;

            // Calculate the sum of current digits and carry
            $sum = $val1 + $val2 + $carry;
            $carry = intdiv($sum, 10); // Update carry
            $newVal = $sum % 10; // Get the last digit of sum

            // Create a new node with the computed value
            $current->next = new ListNode($newVal);
            $current = $current->next;

            // Move to the next nodes in the lists
            if ($l1 !== null) $l1 = $l1->next;
            if ($l2 !== null) $l2 = $l2->next;
        }

        // Return the next of dummy node, which is the head of the result list
        return $dummyHead->next;
    }
}