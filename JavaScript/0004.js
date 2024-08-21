/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
    if (nums1.length > nums2.length) {
        // Ensure nums1 is the smaller array
        [nums1, nums2] = [nums2, nums1];
    }
    
    const m = nums1.length;
    const n = nums2.length;
    let iMin = 0;
    let iMax = m;
    const halfLen = Math.floor((m + n + 1) / 2);

    while (iMin <= iMax) {
        const i = Math.floor((iMin + iMax) / 2);
        const j = halfLen - i;

        const nums1LeftMax = (i === 0) ? -Infinity : nums1[i - 1];
        const nums1RightMin = (i === m) ? Infinity : nums1[i];
        const nums2LeftMax = (j === 0) ? -Infinity : nums2[j - 1];
        const nums2RightMin = (j === n) ? Infinity : nums2[j];

        if (nums1LeftMax <= nums2RightMin && nums2LeftMax <= nums1RightMin) {
            // Perfect partition
            if ((m + n) % 2 === 0) {
                return (Math.max(nums1LeftMax, nums2LeftMax) + Math.min(nums1RightMin, nums2RightMin)) / 2;
            } else {
                return Math.max(nums1LeftMax, nums2LeftMax);
            }
        } else if (nums1LeftMax > nums2RightMin) {
            // Move `i` to the left
            iMax = i - 1;
        } else {
            // Move `i` to the right
            iMin = i + 1;
        }
    }

    throw new Error('Input arrays are not sorted properly.');
};
