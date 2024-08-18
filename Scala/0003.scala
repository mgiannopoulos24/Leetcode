object Solution {
    def lengthOfLongestSubstring(s: String): Int = {
        var maxLength = 0
        var start = 0
        val seen = scala.collection.mutable.Set[Char]()

        for (end <- s.indices) {
            while (seen.contains(s(end))) {
                seen.remove(s(start))
                start += 1
            }
            seen.add(s(end))
            maxLength = math.max(maxLength, end - start + 1)
        }

        maxLength
    }
}
