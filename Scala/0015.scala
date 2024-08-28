object Solution {
    def threeSum(nums: Array[Int]): List[List[Int]] = {
        // Sort the array
        val sortedNums = nums.sorted
        
        // Initialize the result list
        var result = List[List[Int]]()
        
        // Iterate through the sorted array
        for (i <- sortedNums.indices) {
            // Skip the same elements to avoid duplicates
            if (i > 0 && sortedNums(i) == sortedNums(i - 1)) {
                // Skip duplicate element
                // This is equivalent to `continue` in other languages
                // by simply continuing to the next iteration of the loop
                ()
            } else {
                // Two pointers approach
                var left = i + 1
                var right = sortedNums.length - 1
                
                while (left < right) {
                    val sum = sortedNums(i) + sortedNums(left) + sortedNums(right)
                    
                    if (sum == 0) {
                        // Found a triplet
                        result = result :+ List(sortedNums(i), sortedNums(left), sortedNums(right))
                        
                        // Skip duplicates for left and right
                        while (left < right && sortedNums(left) == sortedNums(left + 1)) left += 1
                        while (left < right && sortedNums(right) == sortedNums(right - 1)) right -= 1
                        
                        // Move both pointers
                        left += 1
                        right -= 1
                    } else if (sum < 0) {
                        // Increase the sum by moving left pointer to the right
                        left += 1
                    } else {
                        // Decrease the sum by moving right pointer to the left
                        right -= 1
                    }
                }
            }
        }
        
        // Return the result list
        result
    }
}
