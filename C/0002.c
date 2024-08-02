/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode* dummyHead = (struct ListNode*)malloc(sizeof(struct ListNode));
    dummyHead->val = 0;
    dummyHead->next = NULL;
    struct ListNode* p = l1;
    struct ListNode* q = l2;
    struct ListNode* curr = dummyHead;
    int carry = 0;
    
    while (p != NULL || q != NULL) {
        int x = (p != NULL) ? p->val : 0;
        int y = (q != NULL) ? q->val : 0;
        int sum = carry + x + y;
        carry = sum / 10;
        curr->next = (struct ListNode*)malloc(sizeof(struct ListNode));
        curr = curr->next;
        curr->val = sum % 10;
        curr->next = NULL;
        if (p != NULL) p = p->next;
        if (q != NULL) q = q->next;
    }
    
    if (carry > 0) {
        curr->next = (struct ListNode*)malloc(sizeof(struct ListNode));
        curr = curr->next;
        curr->val = carry;
        curr->next = NULL;
    }
    
    struct ListNode* result = dummyHead->next;
    free(dummyHead);
    return result;
}
