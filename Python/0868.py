class Solution:
    def binaryGap(self, n: int) -> int:
        # Convert n to its binary representation (removing the '0b' prefix)
        binary_rep = bin(n)[2:]

        # Store the indices of '1's
        indices = []

        # Collect all indices where there's a '1' in the binary representation
        for i, bit in enumerate(binary_rep):
            if bit == '1':
                indices.append(i)

        # If there are less than two '1's, return 0
        if len(indices) < 2:
            return 0

        # Calculate the maximum distance between consecutive '1's
        max_distance = 0
        for i in range(1, len(indices)):
            max_distance = max(max_distance, indices[i] - indices[i - 1])

        return max_distance
