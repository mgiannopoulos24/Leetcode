from typing import List

class Solution:
    def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:
        MOD1 = 10**9 + 7
        MOD2 = 10**9 + 13
        BASE1 = 101
        BASE2 = 107

        # Binary search boundaries
        left, right = 0, min(len(p) for p in paths)
        answer = 0

        def is_common(length):
            if length == 0:
                return True

            hash_sets = []

            for path in paths:
                pre_hash1 = pre_hash2 = 0
                set_for_path = set()
                power1 = power2 = 1

                # Precompute powers
                for _ in range(length):
                    power1 = (power1 * BASE1) % MOD1
                    power2 = (power2 * BASE2) % MOD2

                # Compute initial rolling hash
                for i in range(length):
                    pre_hash1 = (pre_hash1 * BASE1 + path[i]) % MOD1
                    pre_hash2 = (pre_hash2 * BASE2 + path[i]) % MOD2

                curr_hash = (pre_hash1, pre_hash2)
                set_for_path.add(curr_hash)

                # Slide window
                for i in range(length, len(path)):
                    # Remove the leftmost element
                    prev_char = path[i - length]
                    pre_hash1 = (pre_hash1 * BASE1 - prev_char * power1 + path[i]) % MOD1
                    pre_hash2 = (pre_hash2 * BASE2 - prev_char * power2 + path[i]) % MOD2
                    # Handle negative mods
                    pre_hash1 = (pre_hash1 + MOD1) % MOD1
                    pre_hash2 = (pre_hash2 + MOD2) % MOD2

                    curr_hash = (pre_hash1, pre_hash2)
                    set_for_path.add(curr_hash)

                hash_sets.append(set_for_path)

            # Get intersection of all sets
            common_hashes = set(hash_sets[0])
            for s in hash_sets[1:]:
                common_hashes &= s
                if not common_hashes:
                    return False
            return True

        # Binary search
        while left <= right:
            mid = (left + right) // 2
            if is_common(mid):
                answer = mid
                left = mid + 1
            else:
                right = mid - 1

        return answer