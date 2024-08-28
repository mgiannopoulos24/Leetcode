#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b) {
    return (*(int *)a - *(int *)b);
}

int** threeSum(int* nums, int numsSize, int* returnSize, int** returnColumnSizes) {
    // Initialize the result array
    int** result = (int**)malloc(sizeof(int*) * numsSize * numsSize); 
    *returnColumnSizes = (int*)malloc(sizeof(int) * numsSize * numsSize);
    int resultIndex = 0;
    
    // Edge case for size less than 3
    if (numsSize < 3) {
        *returnSize = 0;
        return result;
    }
    
    // Sort the array
    qsort(nums, numsSize, sizeof(int), compare);
    
    for (int i = 0; i < numsSize - 2; i++) {
        // Skip duplicates for the first element
        if (i > 0 && nums[i] == nums[i - 1]) {
            continue;
        }
        
        int left = i + 1;
        int right = numsSize - 1;
        
        while (left < right) {
            int sum = nums[i] + nums[left] + nums[right];
            
            if (sum == 0) {
                // Allocate memory for the result triplet
                int* triplet = (int*)malloc(3 * sizeof(int));
                triplet[0] = nums[i];
                triplet[1] = nums[left];
                triplet[2] = nums[right];
                
                result[resultIndex] = triplet;
                (*returnColumnSizes)[resultIndex] = 3;
                resultIndex++;
                
                // Skip duplicates for the second and third elements
                while (left < right && nums[left] == nums[left + 1]) {
                    left++;
                }
                while (left < right && nums[right] == nums[right - 1]) {
                    right--;
                }
                
                left++;
                right--;
            } else if (sum < 0) {
                left++;
            } else {
                right--;
            }
        }
    }
    
    *returnSize = resultIndex;
    return result;
}
