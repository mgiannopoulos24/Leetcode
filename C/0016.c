#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

// Comparison function for qsort
int compare(const void *a, const void *b) {
    return (*(int*)a - *(int*)b);
}

int threeSumClosest(int* nums, int numsSize, int target) {
    if (numsSize < 3) return 0;

    // Sort the array
    qsort(nums, numsSize, sizeof(int), compare);
    
    long closestSum = INT_MAX;

    for (int i = 0; i < numsSize - 2; i++) {
        int left = i + 1;
        int right = numsSize - 1;

        while (left < right) {
            int sum = nums[i] + nums[left] + nums[right];
            
            // Update the closest sum if the current sum is closer to the target
            if (abs(target - sum) < abs(target - closestSum)) {
                closestSum = sum;
            }
            
            // Move the pointers
            if (sum < target) {
                left++;
            } else if (sum > target) {
                right--;
            } else {
                // If the sum is exactly the target, we have found the closest possible sum
                return sum;
            }
        }
    }
    
    return closestSum;
}