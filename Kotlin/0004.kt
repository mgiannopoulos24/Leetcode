class Solution {
    fun findMedianSortedArrays(nums1: IntArray, nums2: IntArray): Double {
        if (nums1.size > nums2.size) {
            // Ensure nums1 is the smaller array
            return findMedianSortedArrays(nums2, nums1)
        }
        
        val m = nums1.size
        val n = nums2.size
        var iMin = 0
        var iMax = m
        val halfLen = (m + n + 1) / 2
        
        while (iMin <= iMax) {
            val i = (iMin + iMax) / 2
            val j = halfLen - i
            
            val nums1LeftMax = if (i == 0) Int.MIN_VALUE else nums1[i - 1]
            val nums1RightMin = if (i == m) Int.MAX_VALUE else nums1[i]
            val nums2LeftMax = if (j == 0) Int.MIN_VALUE else nums2[j - 1]
            val nums2RightMin = if (j == n) Int.MAX_VALUE else nums2[j]
            
            if (nums1LeftMax <= nums2RightMin && nums2LeftMax <= nums1RightMin) {
                // Perfect partition
                return if ((m + n) % 2 == 0) {
                    (maxOf(nums1LeftMax, nums2LeftMax).toDouble() + minOf(nums1RightMin, nums2RightMin).toDouble()) / 2
                } else {
                    maxOf(nums1LeftMax, nums2LeftMax).toDouble()
                }
            } else if (nums1LeftMax > nums2RightMin) {
                // Move `i` to the left
                iMax = i - 1
            } else {
                // Move `i` to the right
                iMin = i + 1
            }
        }
        
        throw IllegalArgumentException("Input arrays are not sorted properly.")
    }
}
