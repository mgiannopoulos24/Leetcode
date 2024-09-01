from typing import List

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # Function to compute the KMP table (also known as "partial match" table)
        def compute_kmp_table(s: str) -> List[int]:
            lps = [0] * len(s)
            length = 0
            i = 1
            
            while i < len(s):
                if s[i] == s[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps
        
        # Reverse the original string
        rev_s = s[::-1]
        
        # Create the new string for KMP processing
        new_string = s + "#" + rev_s
        
        # Compute KMP table for the new_string
        lps = compute_kmp_table(new_string)
        
        # Length of the longest palindromic prefix
        longest_palindromic_prefix_length = lps[-1]
        
        # Construct the shortest palindrome
        to_add = rev_s[:len(s) - longest_palindromic_prefix_length]
        shortest_palindrome = to_add + s
        
        return shortest_palindrome
