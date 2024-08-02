/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    // Create a dictionary to store the number and its index
    let numToIndex = new Map();
    
    // Iterate through the list
    for (let i = 0; i < nums.length; i++) {
        let num = nums[i];
        // Calculate the complement that would sum to the target
        let complement = target - num;
        
        // If the complement is found in the dictionary, return the indices
        if (numToIndex.has(complement)) {
            return [numToIndex.get(complement), i];
        }
        
        // Otherwise, add the number and its index to the dictionary
        numToIndex.set(num, i);
    }
    
    // Return an empty array if no solution is found
    return [];
};