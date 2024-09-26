# @param {String} s
# @return {Integer}
def roman_to_int(s)
    # Hash to store Roman numeral values
    roman_map = {
      'I' => 1,
      'V' => 5,
      'X' => 10,
      'L' => 50,
      'C' => 100,
      'D' => 500,
      'M' => 1000
    }
  
    total = 0
    prev_value = 0
  
    # Loop through the string from right to left
    s.reverse.each_char do |char|
      current_value = roman_map[char]
  
      # If the current value is smaller than the previous one, subtract it
      if current_value < prev_value
        total -= current_value
      else
        total += current_value
      end
  
      prev_value = current_value
    end
  
    total
  end
  