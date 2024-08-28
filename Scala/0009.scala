object Solution {
  def isPalindrome(x: Int): Boolean = {
    // Handle edge cases
    if (x < 0 || (x % 10 == 0 && x != 0)) return false
    
    var original = x
    var reversed = 0
    
    while (original > reversed) {
      reversed = reversed * 10 + (original % 10)
      original /= 10
    }
    
    // For numbers with odd length, `original` will be equal to `reversed / 10`
    original == reversed || original == reversed / 10
  }
}
