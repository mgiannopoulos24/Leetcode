class Solution {
  List<int> twoSum(List<int> nums, int target) {
    // Create a map to store the number and its index
    Map<int, int> numToIndex = {};
    
    // Iterate through the list
    for (int i = 0; i < nums.length; i++) {
      int num = nums[i];
      // Calculate the complement that would sum to the target
      int complement = target - num;
      
      // If the complement is found in the map, return the indices
      if (numToIndex.containsKey(complement)) {
        return [numToIndex[complement]!, i];
      }
      
      // Otherwise, add the number and its index to the map
      numToIndex[num] = i;
    }
    
    // Return an empty list if no solution is found
    return [];
  }
}