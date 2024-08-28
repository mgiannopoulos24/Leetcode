/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
// Priority queue node for heap
typedef struct {
    struct ListNode* node;
} HeapNode;

typedef struct {
    HeapNode* nodes;
    int size;
    int capacity;
} MinHeap;

// Helper functions for MinHeap
void swap(HeapNode* a, HeapNode* b) {
    HeapNode temp = *a;
    *a = *b;
    *b = temp;
}

void heapify(MinHeap* heap, int index) {
    int smallest = index;
    int left = 2 * index + 1;
    int right = 2 * index + 2;

    if (left < heap->size && heap->nodes[left].node->val < heap->nodes[smallest].node->val) {
        smallest = left;
    }

    if (right < heap->size && heap->nodes[right].node->val < heap->nodes[smallest].node->val) {
        smallest = right;
    }

    if (smallest != index) {
        swap(&heap->nodes[index], &heap->nodes[smallest]);
        heapify(heap, smallest);
    }
}

void insertMinHeap(MinHeap* heap, struct ListNode* node) {
    if (heap->size == heap->capacity) {
        heap->capacity *= 2;
        heap->nodes = realloc(heap->nodes, sizeof(HeapNode) * heap->capacity);
    }
    heap->nodes[heap->size].node = node;
    int index = heap->size;
    heap->size++;

    while (index > 0 && heap->nodes[(index - 1) / 2].node->val > heap->nodes[index].node->val) {
        swap(&heap->nodes[index], &heap->nodes[(index - 1) / 2]);
        index = (index - 1) / 2;
    }
}

struct ListNode* extractMin(MinHeap* heap) {
    if (heap->size == 0) return NULL;

    struct ListNode* root = heap->nodes[0].node;
    heap->nodes[0] = heap->nodes[heap->size - 1];
    heap->size--;
    heapify(heap, 0);
    return root;
}

// Main function to merge k sorted lists
struct ListNode* mergeKLists(struct ListNode** lists, int listsSize) {
    if (listsSize == 0) return NULL;

    MinHeap heap;
    heap.size = 0;
    heap.capacity = listsSize;
    heap.nodes = malloc(sizeof(HeapNode) * heap.capacity);

    // Initialize the heap with the head nodes of each list
    for (int i = 0; i < listsSize; i++) {
        if (lists[i] != NULL) {
            insertMinHeap(&heap, lists[i]);
        }
    }

    struct ListNode* dummy = malloc(sizeof(struct ListNode));
    struct ListNode* tail = dummy;

    while (heap.size > 0) {
        struct ListNode* minNode = extractMin(&heap);
        tail->next = minNode;
        tail = tail->next;
        if (minNode->next != NULL) {
            insertMinHeap(&heap, minNode->next);
        }
    }

    tail->next = NULL;
    struct ListNode* result = dummy->next;
    free(dummy);
    free(heap.nodes);
    
    return result;
}

// Function to print linked list (for debugging)
void printList(struct ListNode* head) {
    while (head != NULL) {
        printf("%d ", head->val);
        head = head->next;
    }
    printf("\n");
}
