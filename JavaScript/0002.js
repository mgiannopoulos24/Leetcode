/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */

/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
    // Create a dummy node to simplify operations
    let dummyHead = new ListNode(0);
    let current = dummyHead;
    let carry = 0;

    // Traverse both linked lists
    while (l1 !== null || l2 !== null || carry !== 0) {
        // Get the current values
        let val1 = (l1 !== null) ? l1.val : 0;
        let val2 = (l2 !== null) ? l2.val : 0;

        // Calculate the sum of current digits and carry
        let sum = val1 + val2 + carry;
        carry = Math.floor(sum / 10); // Update carry
        let newVal = sum % 10; // Get the last digit of sum

        // Create a new node with the computed value
        current.next = new ListNode(newVal);
        current = current.next;

        // Move to the next nodes in the lists
        if (l1 !== null) l1 = l1.next;
        if (l2 !== null) l2 = l2.next;
    }

    // Return the next of dummy node, which is the head of the result list
    return dummyHead.next;
};
