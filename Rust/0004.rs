impl Solution {
    pub fn find_median_sorted_arrays(nums1: Vec<i32>, nums2: Vec<i32>) -> f64 {
        let (nums1, nums2) = if nums1.len() > nums2.len() {
            (nums2, nums1) // Ensure nums1 is the smaller array
        } else {
            (nums1, nums2)
        };

        let m = nums1.len();
        let n = nums2.len();

        let mut imin = 0;
        let mut imax = m;
        let half_len = (m + n + 1) / 2;

        while imin <= imax {
            let i = (imin + imax) / 2;
            let j = half_len - i;

            let max_left1 = if i == 0 { i32::MIN } else { nums1[i - 1] };
            let min_right1 = if i == m { i32::MAX } else { nums1[i] };

            let max_left2 = if j == 0 { i32::MIN } else { nums2[j - 1] };
            let min_right2 = if j == n { i32::MAX } else { nums2[j] };

            if max_left1 <= min_right2 && max_left2 <= min_right1 {
                if (m + n) % 2 == 0 {
                    return (f64::max(max_left1 as f64, max_left2 as f64) + f64::min(min_right1 as f64, min_right2 as f64)) / 2.0;
                } else {
                    return f64::max(max_left1 as f64, max_left2 as f64);
                }
            } else if max_left1 > min_right2 {
                imax = i - 1;
            } else {
                imin = i + 1;
            }
        }

        panic!("Input arrays are not sorted properly.");
    }
}
