/**
 * Definition for singly-linked list.
 * class ListNode(_x: Int = 0, _next: ListNode = null) {
 *   var next: ListNode = _next
 *   var x: Int = _x
 * }
 */
import scala.collection.mutable
import scala.collection.mutable.PriorityQueue

object Solution {
    def mergeKLists(lists: Array[ListNode]): ListNode = {
        // Define a case class for the heap to store nodes along with their values
        case class HeapNode(node: ListNode)

        // Create a priority queue (min-heap) using the custom case class
        // PriorityQueue by default is a max-heap, so we reverse the ordering for a min-heap
        implicit val ordering: Ordering[HeapNode] = (a: HeapNode, b: HeapNode) => b.node.x - a.node.x
        val minHeap = mutable.PriorityQueue.empty[HeapNode]

        // Initialize the heap with the head nodes of each list
        for (list <- lists if list != null) {
            minHeap.enqueue(HeapNode(list))
        }

        // Create a dummy node to simplify result list construction
        val dummy = new ListNode()
        var current = dummy

        // Process the heap
        while (minHeap.nonEmpty) {
            val HeapNode(minNode) = minHeap.dequeue()
            current.next = minNode
            current = current.next

            // If there's a next node in the current list, add it to the heap
            if (minNode.next != null) {
                minHeap.enqueue(HeapNode(minNode.next))
            }
        }

        // Return the next node after the dummy node
        dummy.next
    }

    // Helper function to print the linked list (for debugging)
    def printList(head: ListNode): Unit = {
        var current = head
        while (current != null) {
            print(s"${current.x} ")
            current = current.next
        }
        println()
    }
}