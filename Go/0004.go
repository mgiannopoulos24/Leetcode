func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
    m, n := len(nums1), len(nums2)
    
    // Ensure nums1 is the smaller array
    if m > n {
        nums1, nums2 = nums2, nums1
        m, n = n, m
    }
    
    imin, imax, halfLen := 0, m, (m+n+1)/2
    
    for imin <= imax {
        i := (imin + imax) / 2
        j := halfLen - i
        
        if i < m && nums2[j-1] > nums1[i] {
            imin = i + 1
        } else if i > 0 && nums1[i-1] > nums2[j] {
            imax = i - 1
        } else {
            var maxLeft float64
            if i == 0 {
                maxLeft = float64(nums2[j-1])
            } else if j == 0 {
                maxLeft = float64(nums1[i-1])
            } else {
                maxLeft = float64(max(nums1[i-1], nums2[j-1]))
            }
            
            if (m+n)%2 == 1 {
                return maxLeft
            }
            
            var minRight float64
            if i == m {
                minRight = float64(nums2[j])
            } else if j == n {
                minRight = float64(nums1[i])
            } else {
                minRight = float64(min(nums1[i], nums2[j]))
            }
            
            return (maxLeft + minRight) / 2.0
        }
    }
    
    return 0.0
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}
