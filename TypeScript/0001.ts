function twoSum(nums: number[], target: number): number[] {
    // Create a map to store the number and its index
    const numToIndex = new Map<number, number>();
    
    // Iterate through the list
    for (let i = 0; i < nums.length; i++) {
        const num = nums[i];
        // Calculate the complement that would sum to the target
        const complement = target - num;
        
        // If the complement is found in the map, return the indices
        if (numToIndex.has(complement)) {
            return [numToIndex.get(complement)!, i];
        }
        
        // Otherwise, add the number and its index to the map
        numToIndex.set(num, i);
    }
    
    // Return an empty array if no solution is found
    return [];
}