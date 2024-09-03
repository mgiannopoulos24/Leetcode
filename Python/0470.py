# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        Generate a random integer from 1 to 10 using rand7().
        :rtype: int
        """
        while True:
            # Generate a number from 1 to 49
            num = (rand7() - 1) * 7 + rand7()  # Range: 1 to 49
            
            # If the number is within 1 to 40, map it to [1, 10]
            if num <= 40:
                return (num - 1) % 10 + 1
