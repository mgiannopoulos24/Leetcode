object Solution {
    def findMedianSortedArrays(nums1: Array[Int], nums2: Array[Int]): Double = {
        val merged = (nums1 ++ nums2).sorted
        val len = merged.length
        if (len % 2 == 0) {
            // If the merged array has an even length, compute the average of the middle two elements
            val mid1 = merged(len / 2 - 1)
            val mid2 = merged(len / 2)
            (mid1 + mid2) / 2.0
        } else {
            // If the merged array has an odd length, return the middle element
            merged(len / 2)
        }
    }
}
