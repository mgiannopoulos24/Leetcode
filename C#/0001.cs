using System;
using System.Collections.Generic;

public class Solution
{
    public int[] TwoSum(int[] nums, int target)
    {
        // Create a dictionary to store the number and its index
        Dictionary<int, int> numToIndex = new Dictionary<int, int>();
        
        // Iterate through the list
        for (int i = 0; i < nums.Length; i++)
        {
            int num = nums[i];
            // Calculate the complement that would sum to the target
            int complement = target - num;
            
            // If the complement is found in the dictionary, return the indices
            if (numToIndex.ContainsKey(complement))
            {
                return new int[] { numToIndex[complement], i };
            }
            
            // Otherwise, add the number and its index to the dictionary
            numToIndex[num] = i;
        }
        
        // Return an empty array if no solution is found
        return new int[0];
    }
}