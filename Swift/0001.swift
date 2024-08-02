class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        // Create a dictionary to store the number and its index
        var numToIndex = [Int: Int]()
        
        // Iterate through the array
        for (i, num) in nums.enumerated() {
            // Calculate the complement that would sum to the target
            let complement = target - num
            
            // If the complement is found in the dictionary, return the indices
            if let index = numToIndex[complement] {
                return [index, i]
            }
            
            // Otherwise, add the number and its index to the dictionary
            numToIndex[num] = i
        }
        
        // If no solution is found, you might throw an error or return an empty array
        // depending on your preference. Here, we're returning an empty array.
        return []
    }
}
