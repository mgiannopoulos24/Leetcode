# @param {String} s
# @return {Integer}
def length_of_longest_substring(s)
    # Hash to store the last index of each character
    char_index = {}
    left = 0
    max_length = 0
  
    s.each_char.with_index do |char, right|
      if char_index.key?(char) && char_index[char] >= left
        # Move the left pointer to the right of the last occurrence of the current character
        left = char_index[char] + 1
      end
  
      # Update the last index of the current character
      char_index[char] = right
      # Calculate the length of the current window and update max_length if needed
      max_length = [max_length, right - left + 1].max
    end
  
    max_length
  end
  