from typing import List

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def is_self_dividing(number: int) -> bool:
            str_num = str(number)
            for char in str_num:
                digit = int(char)
                if digit == 0 or number % digit != 0:
                    return False
            return True
        
        result = [num for num in range(left, right + 1) if is_self_dividing(num)]
        return result
