#include <stdio.h>

double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    // Ensure that nums1 is the smaller array to minimize the binary search range
    if (nums1Size > nums2Size) {
        return findMedianSortedArrays(nums2, nums2Size, nums1, nums1Size);
    }
    
    int m = nums1Size;
    int n = nums2Size;
    int halfLen = (m + n + 1) / 2;
    int imin = 0, imax = m;
    
    while (imin <= imax) {
        int i = (imin + imax) / 2;
        int j = halfLen - i;
        
        if (i < m && nums1[i] < nums2[j - 1]) {
            imin = i + 1; // i is too small, must increase it
        } else if (i > 0 && nums1[i - 1] > nums2[j]) {
            imax = i - 1; // i is too large, must decrease it
        } else {
            // i is perfect
            int max_of_left;
            if (i == 0) {
                max_of_left = nums2[j - 1];
            } else if (j == 0) {
                max_of_left = nums1[i - 1];
            } else {
                max_of_left = (nums1[i - 1] > nums2[j - 1]) ? nums1[i - 1] : nums2[j - 1];
            }
            
            if ((m + n) % 2 == 1) {
                return max_of_left;
            }
            
            int min_of_right;
            if (i == m) {
                min_of_right = nums2[j];
            } else if (j == n) {
                min_of_right = nums1[i];
            } else {
                min_of_right = (nums1[i] < nums2[j]) ? nums1[i] : nums2[j];
            }
            
            return (max_of_left + min_of_right) / 2.0;
        }
    }
    
    return 0.0; // Should never reach here if the input arrays are valid
}
