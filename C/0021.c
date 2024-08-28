/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
// Function to merge two sorted linked lists
struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    // Create a dummy node to simplify edge cases
    struct ListNode dummy;
    dummy.next = NULL;
    struct ListNode* current = &dummy;

    // Traverse both lists
    while (list1 != NULL && list2 != NULL) {
        if (list1->val <= list2->val) {
            current->next = list1;
            list1 = list1->next;
        } else {
            current->next = list2;
            list2 = list2->next;
        }
        current = current->next;
    }

    // If there are remaining nodes in list1 or list2, append them
    if (list1 != NULL) {
        current->next = list1;
    } else {
        current->next = list2;
    }

    // Return the head of the merged list
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
