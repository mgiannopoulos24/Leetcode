object Solution {
    def twoSum(nums: Array[Int], target: Int): Array[Int] = {
        val numToIndex = scala.collection.mutable.Map[Int, Int]()

        var result: Option[Array[Int]] = None

        for (i <- nums.indices) {
            val complement = target - nums(i)
            numToIndex.get(complement) match {
                case Some(index) =>
                    result = Some(Array(index, i))
                    // No need to break, just continue to the end of the loop
                case None =>
                    numToIndex(nums(i)) = i
            }
        }

        result.getOrElse(throw new IllegalArgumentException("No two sum solution"))
    }
}
