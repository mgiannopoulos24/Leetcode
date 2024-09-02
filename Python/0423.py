class Solution:
    def originalDigits(self, s: str) -> str:
        from collections import Counter
        
        # Count frequency of each character in the input string
        count = Counter(s)
        
        # Initialize a dictionary to store the count of each digit
        digit_count = [0] * 10
        
        # Count digits with unique characters first
        digit_count[0] = count['z']  # 'z' is unique to "zero"
        digit_count[2] = count['w']  # 'w' is unique to "two"
        digit_count[4] = count['u']  # 'u' is unique to "four"
        digit_count[6] = count['x']  # 'x' is unique to "six"
        digit_count[8] = count['g']  # 'g' is unique to "eight"
        
        # Calculate counts of other digits using remaining characters
        digit_count[3] = count['h'] - digit_count[8]  # 'h' is in "three" and "eight"
        digit_count[5] = count['f'] - digit_count[4]  # 'f' is in "five" and "four"
        digit_count[7] = count['s'] - digit_count[6]  # 's' is in "seven" and "six"
        digit_count[1] = count['o'] - digit_count[0] - digit_count[2] - digit_count[4]  # 'o' is in "one", "zero", "two", and "four"
        digit_count[9] = count['i'] - digit_count[5] - digit_count[6] - digit_count[8]  # 'i' is in "nine", "five", "six", and "eight"
        
        # Construct the result
        result = []
        for digit in range(10):
            result.append(str(digit) * digit_count[digit])
        
        return ''.join(result)
