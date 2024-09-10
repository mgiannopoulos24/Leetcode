impl Solution {
    pub fn max_area(height: Vec<i32>) -> i32 {
        let mut left = 0;
        let mut right = height.len() - 1;
        let mut max_area = 0;

        while left < right {
            let width = (right - left) as i32;
            let current_height = height[left].min(height[right]);
            let area = width * current_height;
            max_area = max_area.max(area);

            // Move the pointer pointing to the shorter line
            if height[left] < height[right] {
                left += 1;
            } else {
                right -= 1;
            }
        }

        max_area
    }
}
