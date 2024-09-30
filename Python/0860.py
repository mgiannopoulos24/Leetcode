from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # Counters for $5 and $10 bills
        five = 0
        ten = 0
        
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if five > 0:
                    five -= 1
                    ten += 1
                else:
                    return False
            elif bill == 20:
                # Prefer to give one $10 bill and one $5 bill if possible
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1
                # If above is not possible, try giving three $5 bills
                elif five >= 3:
                    five -= 3
                else:
                    return False
        
        return True
