#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

// Helper function to sort the array using quicksort
void quicksort(int* arr, int left, int right) {
    if (left < right) {
        int pivot = arr[(left + right) / 2];
        int i = left, j = right;
        while (i <= j) {
            while (arr[i] < pivot) i++;
            while (arr[j] > pivot) j--;
            if (i <= j) {
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
                i++;
                j--;
            }
        }
        if (left < j) quicksort(arr, left, j);
        if (i < right) quicksort(arr, i, right);
    }
}

// Helper function to check if a combination already exists
bool existsInResult(int** result, int returnSize, int* quad) {
    for (int i = 0; i < returnSize; i++) {
        if (result[i][0] == quad[0] && result[i][1] == quad[1] &&
            result[i][2] == quad[2] && result[i][3] == quad[3]) {
            return true;
        }
    }
    return false;
}

// Main function to find all unique quadruplets
int** fourSum(int* nums, int numsSize, int target, int* returnSize, int** returnColumnSizes) {
    quicksort(nums, 0, numsSize - 1);

    int** result = malloc(1000 * sizeof(int*)); // Initial allocation
    int resultCapacity = 1000;
    *returnColumnSizes = malloc(1000 * sizeof(int));
    int returnCapacity = 1000;

    *returnSize = 0;

    for (int i = 0; i < numsSize - 3; i++) {
        if (i > 0 && nums[i] == nums[i - 1]) continue;
        for (int j = i + 1; j < numsSize - 2; j++) {
            if (j > i + 1 && nums[j] == nums[j - 1]) continue;

            int left = j + 1;
            int right = numsSize - 1;

            while (left < right) {
                // Use long long for sum calculation to avoid overflow
                long long sum = (long long)nums[i] + (long long)nums[j] + (long long)nums[left] + (long long)nums[right];
                if (sum == target) {
                    int* quad = malloc(4 * sizeof(int));
                    quad[0] = nums[i];
                    quad[1] = nums[j];
                    quad[2] = nums[left];
                    quad[3] = nums[right];

                    if (!existsInResult(result, *returnSize, quad)) {
                        if (*returnSize >= resultCapacity) {
                            resultCapacity *= 2;
                            result = realloc(result, resultCapacity * sizeof(int*));
                        }
                        result[*returnSize] = quad;

                        if (*returnSize >= returnCapacity) {
                            returnCapacity *= 2;
                            *returnColumnSizes = realloc(*returnColumnSizes, returnCapacity * sizeof(int));
                        }
                        (*returnColumnSizes)[*returnSize] = 4;
                        (*returnSize)++;
                    } else {
                        free(quad);
                    }
                    left++;
                    right--;
                    while (left < right && nums[left] == nums[left - 1]) left++;
                    while (left < right && nums[right] == nums[right + 1]) right--;
                } else if (sum < target) {
                    left++;
                } else {
                    right--;
                }
            }
        }
    }

    return result;
}