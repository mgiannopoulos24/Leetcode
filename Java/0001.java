import java.util.HashMap;
import java.util.Map;

public class Solution {
    public int[] twoSum(int[] nums, int target) {
        // Create a map to store the number and its index
        Map<Integer, Integer> numToIndex = new HashMap<>();
        
        // Iterate through the array
        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];
            int complement = target - num;
            
            // If the complement is found in the map, return the indices
            if (numToIndex.containsKey(complement)) {
                return new int[] {numToIndex.get(complement), i};
            }
            
            // Otherwise, add the number and its index to the map
            numToIndex.put(num, i);
        }
        
        // Return an empty array if no solution is found (though the problem assumes one exists)
        return new int[0];
    }
}
