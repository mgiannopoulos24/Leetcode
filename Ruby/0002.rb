# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val = 0, _next = nil)
#         @val = val
#         @next = _next
#     end
# end
# @param {ListNode} l1
# @param {ListNode} l2
# @return {ListNode}
def add_two_numbers(l1, l2)
    dummy_head = ListNode.new(0) # Create a dummy head to simplify the code
    current = dummy_head         # Pointer to construct the new linked list
    carry = 0                   # Initialize carry to 0
  
    # Traverse both linked lists
    while l1 || l2 || carry != 0
      # Get the current values from the nodes, if present
      val1 = l1 ? l1.val : 0
      val2 = l2 ? l2.val : 0
  
      # Calculate the sum of current digits and the carry
      sum = val1 + val2 + carry
  
      # Update carry for the next digit
      carry = sum / 10
  
      # Create a new node with the digit part of the sum
      current.next = ListNode.new(sum % 10)
      current = current.next
  
      # Move to the next nodes in the input lists
      l1 = l1 ? l1.next : nil
      l2 = l2 ? l2.next : nil
    end
  
    # Return the next node of the dummy head, which is the start of the result list
    dummy_head.next
  end