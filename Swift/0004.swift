class Solution {
    func findMedianSortedArrays(_ nums1: [Int], _ nums2: [Int]) -> Double {
        let A = nums1
        let B = nums2
        let m = A.count
        let n = B.count
        
        // Ensure that A is the smaller array
        if m > n {
            return findMedianSortedArrays(B, A)
        }
        
        var imin = 0
        var imax = m
        let halfLen = (m + n + 1) / 2
        
        while imin <= imax {
            let i = (imin + imax) / 2
            let j = halfLen - i
            
            if i < m && B[j - 1] > A[i] {
                imin = i + 1
            } else if i > 0 && A[i - 1] > B[j] {
                imax = i - 1
            } else {
                let maxLeftA = (i == 0) ? Int.min : A[i - 1]
                let minRightA = (i == m) ? Int.max : A[i]
                let maxLeftB = (j == 0) ? Int.min : B[j - 1]
                let minRightB = (j == n) ? Int.max : B[j]
                
                if (m + n) % 2 == 1 {
                    return Double(max(maxLeftA, maxLeftB))
                } else {
                    return (Double(max(maxLeftA, maxLeftB)) + Double(min(minRightA, minRightB))) / 2.0
                }
            }
        }
        
        fatalError("Input arrays are not sorted or of incorrect length.")
    }
}
