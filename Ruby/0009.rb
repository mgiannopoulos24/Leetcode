# @param {Integer} x
# @return {Boolean}
def is_palindrome(x)
    # Negative numbers and numbers ending in zero (except zero itself) cannot be palindromes.
    return false if x < 0 || (x % 10 == 0 && x != 0)
    
    original = x
    reversed = 0
    
    # Reverse the number
    while x > 0
      digit = x % 10 # Get the last digit
      reversed = reversed * 10 + digit # Build the reversed number
      x /= 10 # Remove the last digit from x
    end
    
    # Compare the reversed number with the original number
    original == reversed
  end
  