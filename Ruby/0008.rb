# @param {String} s
# @return {Integer}
def my_atoi(s)
    # Define the 32-bit signed integer boundaries
    int_min = -2**31
    int_max = 2**31 - 1

    # Trim leading whitespace
    s = s.strip
    return 0 if s.empty?

    # Initialize sign and result
    sign = 1
    result = 0
    i = 0

    # Determine the sign
    if s[i] == '-'
        sign = -1
        i += 1
    elsif s[i] == '+'
        i += 1
    end

    # Process the digits
    while i < s.length && s[i].match?(/\d/)
        digit = s[i].to_i
        
        # Check for overflow before updating the result
        if result > (int_max - digit) / 10
            return sign == 1 ? int_max : int_min
        end
        
        result = result * 10 + digit
        i += 1
    end

    sign * result
end
