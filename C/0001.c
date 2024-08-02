#include <stdio.h>
#include <stdlib.h>

#define HASH_SIZE 10000 // Size of the hash table

// Structure to represent the hash table
typedef struct {
    int key;
    int value;
    int used;
} HashEntry;

// Hash function
int hash(int key) {
    return abs(key) % HASH_SIZE;
}

// Function to insert into hash table
void insert(HashEntry* hash_table, int key, int value) {
    int idx = hash(key);
    while (hash_table[idx].used && hash_table[idx].key != key) {
        idx = (idx + 1) % HASH_SIZE;
    }
    hash_table[idx].key = key;
    hash_table[idx].value = value;
    hash_table[idx].used = 1;
}

// Function to search in hash table
int search(HashEntry* hash_table, int key) {
    int idx = hash(key);
    while (hash_table[idx].used) {
        if (hash_table[idx].key == key) {
            return hash_table[idx].value;
        }
        idx = (idx + 1) % HASH_SIZE;
    }
    return -1;
}

// Function to find two indices that sum up to the target
int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    HashEntry* hash_table = (HashEntry*)calloc(HASH_SIZE, sizeof(HashEntry));
    int* result = (int*)malloc(2 * sizeof(int));
    *returnSize = 2;

    for (int i = 0; i < numsSize; ++i) {
        int complement = target - nums[i];
        int index = search(hash_table, complement);
        if (index != -1) {
            result[0] = index;
            result[1] = i;
            free(hash_table);
            return result;
        }
        insert(hash_table, nums[i], i);
    }

    free(hash_table);
    *returnSize = 0;
    return NULL; // No solution found
}
