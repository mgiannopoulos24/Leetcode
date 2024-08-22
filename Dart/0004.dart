import 'dart:math';

class Solution {
  double findMedianSortedArrays(List<int> nums1, List<int> nums2) {
    // Ensure nums1 is the smaller array
    if (nums1.length > nums2.length) {
      return findMedianSortedArrays(nums2, nums1);
    }

    int m = nums1.length;
    int n = nums2.length;
    int imin = 0;
    int imax = m;
    double halfLen = (m + n + 1) / 2.0;

    while (imin <= imax) {
      int i = (imin + imax) ~/ 2;
      int j = (halfLen - i).toInt();

      // Partition values
      double maxX = i == 0 ? double.negativeInfinity : nums1[i - 1].toDouble();
      double minX = i == m ? double.infinity : nums1[i].toDouble();
      double maxY = j == 0 ? double.negativeInfinity : nums2[j - 1].toDouble();
      double minY = j == n ? double.infinity : nums2[j].toDouble();

      if (maxX <= minY && maxY <= minX) {
        if ((m + n) % 2 == 0) {
          return (max(maxX, maxY) + min(minX, minY)) / 2.0;
        } else {
          return max(maxX, maxY);
        }
      } else if (maxX > minY) {
        imax = i - 1;
      } else {
        imin = i + 1;
      }
    }

    throw ArgumentError("Input arrays are not sorted or invalid");
  }
}
