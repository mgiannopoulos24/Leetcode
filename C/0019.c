/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

// Function to remove the nth node from the end of the list
struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
    // Create a dummy node to simplify edge cases (like removing the head node)
    struct ListNode dummy;
    dummy.next = head;
    
    // Initialize two pointers
    struct ListNode* fast = &dummy;
    struct ListNode* slow = &dummy;
    
    // Move fast pointer n+1 steps ahead so that the gap between fast and slow is n
    for (int i = 0; i <= n; i++) {
        fast = fast->next;
    }
    
    // Move both fast and slow pointers until fast reaches the end
    while (fast != NULL) {
        fast = fast->next;
        slow = slow->next;
    }
    
    // Remove the nth node from end
    struct ListNode* nodeToRemove = slow->next;
    slow->next = slow->next->next;
    
    // Free the memory of the removed node
    free(nodeToRemove);
    
    return dummy.next;
}

// Helper function to create a new node
struct ListNode* createNode(int val) {
    struct ListNode* newNode = (struct ListNode*)malloc(sizeof(struct ListNode));
    newNode->val = val;
    newNode->next = NULL;
    return newNode;
}

// Helper function to print the list
void printList(struct ListNode* head) {
    while (head != NULL) {
        printf("%d ", head->val);
        head = head->next;
    }
    printf("\n");
}