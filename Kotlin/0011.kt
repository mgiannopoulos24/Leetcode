class Solution {
    fun maxArea(height: IntArray): Int {
        var left = 0
        var right = height.size - 1
        var maxArea = 0

        while (left < right) {
            val width = right - left
            val currentHeight = minOf(height[left], height[right])
            val area = width * currentHeight
            maxArea = maxOf(maxArea, area)

            // Move the pointer pointing to the shorter line
            if (height[left] < height[right]) {
                left++
            } else {
                right--
            }
        }

        return maxArea
    }
}
