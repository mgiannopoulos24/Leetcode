func twoSum(nums []int, target int) []int {
    // Create a map to store the number and its index
    numToIndex := make(map[int]int)
    
    // Iterate through the slice
    for i, num := range nums {
        // Calculate the complement that would sum to the target
        complement := target - num
        
        // If the complement is found in the map, return the indices
        if index, found := numToIndex[complement]; found {
            return []int{index, i}
        }
        
        // Otherwise, add the number and its index to the map
        numToIndex[num] = i
    }
    
    // Return an empty slice if no solution is found (though problem guarantees one)
    return []int{}
}