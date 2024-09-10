func maxArea(height []int) int {
    left := 0
    right := len(height) - 1
    maxArea := 0

    for left < right {
        width := right - left
        currentHeight := min(height[left], height[right])
        area := width * currentHeight
        if area > maxArea {
            maxArea = area
        }

        // Move the pointer pointing to the shorter line
        if height[left] < height[right] {
            left++
        } else {
            right--
        }
    }

    return maxArea
}

// Helper function to find the minimum of two integers
func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}
