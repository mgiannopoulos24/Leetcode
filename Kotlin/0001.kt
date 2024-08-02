class Solution{
    fun twoSum(nums: IntArray, target: Int): IntArray {
        // Create a map to store the number and its index
        val numToIndex = mutableMapOf<Int, Int>()
        
        // Iterate through the array
        for ((index, num) in nums.withIndex()) {
            // Calculate the complement that would sum to the target
            val complement = target - num
            
            // If the complement is found in the map, return the indices
            numToIndex[complement]?.let {
                return intArrayOf(it, index)
            }
            
            // Otherwise, add the number and its index to the map
            numToIndex[num] = index
        }
        
        // Return an empty array if no solution is found (though problem guarantees one)
        return intArrayOf()
    }
}