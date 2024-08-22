# @param {String} s
# @return {String}
def longest_palindrome(s)
    return "" if s.empty?
  
    start = 0
    max_len = 1
    length = s.length
  
    (0...length).each do |i|
      # Find the longest palindrome centered at i (odd length)
      l1, r1 = expand_around_center(s, i, i)
      # Find the longest palindrome centered between i and i + 1 (even length)
      l2, r2 = expand_around_center(s, i, i + 1)
  
      # Update the maximum length palindrome if necessary
      if r1 - l1 > max_len
        start = l1
        max_len = r1 - l1
      end
      if r2 - l2 > max_len
        start = l2
        max_len = r2 - l2
      end
    end
  
    s[start, max_len]
  end
  
  # Helper function to expand around the center and return the bounds of the palindrome
  def expand_around_center(s, left, right)
    while left >= 0 && right < s.length && s[left] == s[right]
      left -= 1
      right += 1
    end
    # Return the start and end indices of the palindrome
    [left + 1, right]
  end
  