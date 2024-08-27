class Solution {
    fun reverse(x: Int): Int {
        var rev = 0
        var num = x
        val sign = if (x < 0) -1 else 1
        num = Math.abs(num)

        while (num != 0) {
            val pop = num % 10
            num /= 10

            // Check for overflow before updating rev
            if (rev > Int.MAX_VALUE / 10 || (rev == Int.MAX_VALUE / 10 && pop > 7)) return 0
            if (rev < Int.MIN_VALUE / 10 || (rev == Int.MIN_VALUE / 10 && pop < -8)) return 0

            rev = rev * 10 + pop
        }

        return rev * sign
    }
}
