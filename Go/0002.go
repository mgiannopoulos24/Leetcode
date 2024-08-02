func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
    // Create a dummy node to simplify operations
    dummyHead := &ListNode{}
    current := dummyHead
    carry := 0

    // Traverse both lists
    for l1 != nil || l2 != nil || carry != 0 {
        // Get the current values
        val1 := 0
        val2 := 0

        if l1 != nil {
            val1 = l1.Val
            l1 = l1.Next
        }

        if l2 != nil {
            val2 = l2.Val
            l2 = l2.Next
        }

        // Calculate the sum of current digits and carry
        sum := val1 + val2 + carry
        carry = sum / 10
        newNode := &ListNode{Val: sum % 10}

        // Append the new node to the result list
        current.Next = newNode
        current = newNode
    }

    // Return the next of dummy node, which is the head of the result list
    return dummyHead.Next
}