def reverse(x)
    # Limits for 32-bit signed integer range
    int_min = -2**31
    int_max = 2**31 - 1
  
    # Handle negative numbers
    sign = x < 0 ? -1 : 1
    x = x.abs
  
    reversed = 0
    while x > 0
      pop = x % 10
      x /= 10
  
      # Check for overflow before updating reversed
      if reversed > (int_max - pop) / 10
        return 0
      end
  
      reversed = reversed * 10 + pop
    end
  
    # Restore the sign and check if the result is within the 32-bit integer range
    reversed *= sign
  
    if reversed < int_min || reversed > int_max
      return 0
    end
  
    reversed
  end
  