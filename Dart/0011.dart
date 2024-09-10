class Solution {
  int maxArea(List<int> height) {
    int left = 0;
    int right = height.length - 1;
    int maxArea = 0;

    while (left < right) {
      int width = right - left;
      int currentHeight = (height[left] < height[right]) ? height[left] : height[right];
      int area = width * currentHeight;
      maxArea = (area > maxArea) ? area : maxArea;

      // Move the pointer pointing to the shorter line
      if (height[left] < height[right]) {
        left++;
      } else {
        right--;
      }
    }

    return maxArea;
  }
}
