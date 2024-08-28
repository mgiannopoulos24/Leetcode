object Solution {
    def threeSumClosest(nums: Array[Int], target: Int): Int = {
        // Sort the array
        val sortedNums = nums.sorted
        
        // Initialize the closest sum with a large value
        var closestSum = Int.MaxValue
        
        // Iterate through the array
        for (i <- sortedNums.indices) {
            // Use two pointers for the remaining elements
            var left = i + 1
            var right = sortedNums.length - 1
            
            while (left < right) {
                val sum = sortedNums(i) + sortedNums(left) + sortedNums(right)
                
                // Update closestSum if the current sum is closer to the target
                if (Math.abs(sum - target) < Math.abs(closestSum - target)) {
                    closestSum = sum
                }
                
                // Move pointers based on comparison with target
                if (sum < target) {
                    left += 1
                } else if (sum > target) {
                    right -= 1
                } else {
                    // If sum exactly matches the target, update closestSum and exit the loop
                    closestSum = sum
                    // Break out of the inner while loop
                    left = right // This will exit the loop as left >= right
                }
            }
        }
        
        // Return the closest sum found
        closestSum
    }
}
