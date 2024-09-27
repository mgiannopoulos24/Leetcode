from typing import List

class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        n = len(row)
        # Create a position map to locate the positions quickly
        position = {person: i for i, person in enumerate(row)}
        
        swaps = 0
        
        for i in range(0, n, 2):
            first_person = row[i]
            correct_partner = first_person ^ 1  # XOR with 1 will give the partner
            
            if row[i + 1] != correct_partner:
                # Get the current index of the correct partner
                partner_index = position[correct_partner]
                
                # Swap the person at row[i+1] with the correct partner
                row[i + 1], row[partner_index] = row[partner_index], row[i + 1]
                
                # Update the positions in the hashmap
                position[row[partner_index]] = partner_index
                position[row[i + 1]] = i + 1
                
                swaps += 1
        
        return swaps
