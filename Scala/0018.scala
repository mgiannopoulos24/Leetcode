object Solution {
  def fourSum(nums: Array[Int], target: Int): List[List[Int]] = {
    // Sort the array
    val sortedNums = nums.sorted

    // Initialize a set to store the unique quadruplets
    var resultSet = Set[List[Int]]()

    // Iterate over each element to find possible quadruplets
    for (i <- sortedNums.indices.dropRight(3)) {
      // Avoid duplicates for the first element
      if (i > 0 && sortedNums(i) == sortedNums(i - 1)) {
        // Skip the duplicate element
        ()
      } else {
        for (j <- (i + 1) until sortedNums.length - 1) {
          // Avoid duplicates for the second element
          if (j > i + 1 && sortedNums(j) == sortedNums(j - 1)) {
            // Skip the duplicate element
            ()
          } else {
            // Two pointers approach for the remaining two elements
            var left = j + 1
            var right = sortedNums.length - 1

            while (left < right) {
              val sum = sortedNums(i).toLong + sortedNums(j).toLong + sortedNums(left).toLong + sortedNums(right).toLong

              if (sum == target) {
                // Add the quadruplet to the set if it's not already present
                resultSet += List(sortedNums(i), sortedNums(j), sortedNums(left), sortedNums(right))
                // Move both pointers
                left += 1
                right -= 1
                // Skip duplicates for the third element
                while (left < right && sortedNums(left) == sortedNums(left - 1)) left += 1
                // Skip duplicates for the fourth element
                while (left < right && sortedNums(right) == sortedNums(right + 1)) right -= 1
              } else if (sum < target) {
                left += 1
              } else {
                right -= 1
              }
            }
          }
        }
      }
    }

    // Convert the set to a list of lists
    resultSet.toList
  }
}
