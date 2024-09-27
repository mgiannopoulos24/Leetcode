class Solution:
    def rotatedDigits(self, n: int) -> int:
        def is_good_number(x):
            rotation_map = {'0': '0', '1': '1', '2': '5', '5': '2', '6': '9', '8': '8', '9': '6'}
            original = str(x)
            rotated = []
            for char in original:
                if char not in rotation_map:
                    return False
                rotated.append(rotation_map[char])
            rotated_number = int(''.join(rotated))
            return rotated_number != x
        
        count = 0
        for i in range(1, n + 1):
            if is_good_number(i):
                count += 1
        
        return count
