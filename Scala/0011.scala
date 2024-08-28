object Solution {
  def maxArea(height: Array[Int]): Int = {
    var left = 0
    var right = height.length - 1
    var maxArea = 0

    while (left < right) {
      // Calculate the width and height
      val width = right - left
      val currentHeight = Math.min(height(left), height(right))
      val currentArea = width * currentHeight
      
      // Update maxArea if the current area is larger
      maxArea = Math.max(maxArea, currentArea)
      
      // Move the pointer pointing to the shorter line
      if (height(left) < height(right)) {
        left += 1
      } else {
        right -= 1
      }
    }

    maxArea
  }
}
