class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        # Step 1: Generate the Gray code sequence for n
        gray_code = [i ^ (i >> 1) for i in range(1 << n)]
        
        # Step 2: Find the index of `start` in the Gray code sequence
        start_index = gray_code.index(start)
        
        # Step 3: Rotate the sequence so that it starts with `start`
        return gray_code[start_index:] + gray_code[:start_index]
