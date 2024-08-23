# @param {String} s
# @param {Integer} num_rows
# @return {String}
def convert(s, num_rows)
    return s if num_rows == 1 || num_rows >= s.length
  
    # Initialize an array of empty strings for each row
    rows = Array.new(num_rows, '')
  
    current_row = 0
    going_down = false
  
    # Traverse each character in the string
    s.each_char do |char|
      rows[current_row] += char
  
      # Change direction if we're at the top or bottom row
      if current_row == 0 || current_row == num_rows - 1
        going_down = !going_down
      end
  
      # Move to the next row
      current_row += going_down ? 1 : -1
    end
  
    # Concatenate all rows to get the final result
    rows.join('')
  end
  