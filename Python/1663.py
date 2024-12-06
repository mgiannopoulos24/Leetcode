class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        # Initialize the result string with 'a' repeated n times (the smallest lexicographical character)
        result = ['a'] * n
        # Adjust k to account for the initial 'a's, as each 'a' has a value of 1
        k -= n
        
        # Start filling the string from the end
        i = n - 1
        while k > 0:
            # Determine how much we can add to the current position
            # We can add at most 25 since 'z' has a value of 26 and 'a' has a value of 1
            add_value = min(25, k)
            result[i] = chr(ord('a') + add_value)
            k -= add_value
            i -= 1
        
        # Join the list of characters into a string and return it
        return ''.join(result)
