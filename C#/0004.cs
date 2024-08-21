public class Solution {
    public double FindMedianSortedArrays(int[] nums1, int[] nums2) {
        // Ensure nums1 is the smaller array
        if (nums1.Length > nums2.Length) {
            int[] temp = nums1;
            nums1 = nums2;
            nums2 = temp;
        }

        int m = nums1.Length;
        int n = nums2.Length;
        int imin = 0, imax = m, halfLen = (m + n + 1) / 2;

        while (imin <= imax) {
            int i = (imin + imax) / 2;
            int j = halfLen - i;

            // i is too small, need to increase it
            if (i < m && nums2[j - 1] > nums1[i]) {
                imin = i + 1;
            }
            // i is too big, need to decrease it
            else if (i > 0 && nums1[i - 1] > nums2[j]) {
                imax = i - 1;
            }
            // i is perfect
            else {
                int maxLeft1 = (i == 0) ? int.MinValue : nums1[i - 1];
                int minRight1 = (i == m) ? int.MaxValue : nums1[i];
                int maxLeft2 = (j == 0) ? int.MinValue : nums2[j - 1];
                int minRight2 = (j == n) ? int.MaxValue : nums2[j];

                if ((m + n) % 2 == 0) {
                    return (Math.Max(maxLeft1, maxLeft2) + Math.Min(minRight1, minRight2)) / 2.0;
                } else {
                    return Math.Max(maxLeft1, maxLeft2);
                }
            }
        }

        throw new ArgumentException("Input arrays are not sorted.");
    }
}
