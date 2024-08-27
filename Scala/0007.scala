object Solution {
  def reverse(x: Int): Int = {
    var rev = 0
    var num = x
    
    while (num != 0) {
      // Extract the last digit
      val pop = num % 10
      num /= 10
      
      // Check for overflow/underflow before updating rev
      if (rev > Int.MaxValue / 10 || (rev == Int.MaxValue / 10 && pop > 7)) return 0
      if (rev < Int.MinValue / 10 || (rev == Int.MinValue / 10 && pop < -8)) return 0
      
      rev = rev * 10 + pop
    }
    
    rev
  }
}
