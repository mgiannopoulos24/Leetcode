function findMedianSortedArrays(nums1: number[], nums2: number[]): number {
    // Ensure nums1 is the smaller array
    if (nums1.length > nums2.length) {
        [nums1, nums2] = [nums2, nums1];
    }
    
    const m = nums1.length;
    const n = nums2.length;
    let imin = 0, imax = m, halfLen = Math.floor((m + n + 1) / 2);
    
    while (imin <= imax) {
        const i = Math.floor((imin + imax) / 2);
        const j = halfLen - i;
        
        // Check if we are in the right position for partition
        if (i < m && nums2[j - 1] > nums1[i]) {
            imin = i + 1; // i is too small
        } else if (i > 0 && nums1[i - 1] > nums2[j]) {
            imax = i - 1; // i is too large
        } else {
            // i is perfect
            let maxLeft: number;
            if (i === 0) maxLeft = nums2[j - 1];
            else if (j === 0) maxLeft = nums1[i - 1];
            else maxLeft = Math.max(nums1[i - 1], nums2[j - 1]);
            
            if ((m + n) % 2 === 1) return maxLeft;
            
            let minRight: number;
            if (i === m) minRight = nums2[j];
            else if (j === n) minRight = nums1[i];
            else minRight = Math.min(nums1[i], nums2[j]);
            
            return (maxLeft + minRight) / 2;
        }
    }
    
    throw new Error("Input arrays are not sorted properly");
}
