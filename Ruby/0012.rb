# @param {Integer} num
# @return {String}
def int_to_roman(num)
    # Define the values and symbols
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
  
    result = ""
  
    # Iterate over the values and symbols
    values.each_with_index do |value, index|
      while num >= value
        result += symbols[index]
        num -= value
      end
    end
  
    result
  end