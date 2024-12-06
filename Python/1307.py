class Solution:
    def isSolvable(self, words, result):
        from collections import defaultdict

        # Collect unique characters and non-zero leading characters
        char_set = set()
        non_zero_chars = set()
        for word in words + [result]:
            char_set.update(word)
            if len(word) > 1:
                non_zero_chars.add(word[0])

        if len(char_set) > 10:
            return False  # Cannot assign unique digits to more than 10 characters

        # Assign indices to characters
        char_list = list(char_set)
        char_index = {c: i for i, c in enumerate(char_list)}
        n = len(char_list)

        # Compute weights for each character
        weights = [0] * n
        for word in words:
            factor = 1
            for c in reversed(word):
                idx = char_index[c]
                weights[idx] += factor
                factor *= 10
        factor = 1
        for c in reversed(result):
            idx = char_index[c]
            weights[idx] -= factor
            factor *= 10

        # Sort characters by absolute weight in decreasing order
        char_weight = list(zip(char_list, weights))
        char_weight.sort(key=lambda x: -abs(x[1]))
        char_list = [cw[0] for cw in char_weight]
        weights = [cw[1] for cw in char_weight]

        assigned = {}
        used_digits = [False] * 10

        def dfs(idx, total):
            if idx == n:
                return total == 0
            c = char_list[idx]
            w = weights[idx]
            possible_digits = []
            for d in range(10):
                if not used_digits[d]:
                    if d == 0 and c in non_zero_chars:
                        continue  # Leading character cannot be zero
                    possible_digits.append(d)
            if not possible_digits:
                return False
            # Try digits in order that may reduce total towards zero
            if w > 0:
                possible_digits.sort(reverse=True)
            else:
                possible_digits.sort()
            for d in possible_digits:
                assigned[c] = d
                used_digits[d] = True
                new_total = total + w * d
                # Recompute min_total and max_total with remaining characters
                min_total = new_total
                max_total = new_total
                success = True
                for i in range(idx + 1, n):
                    c2 = char_list[i]
                    w2 = weights[i]
                    digits = []
                    for d2 in range(10):
                        if not used_digits[d2]:
                            if d2 == 0 and c2 in non_zero_chars:
                                continue
                            digits.append(d2)
                    if not digits:
                        success = False
                        break
                    min_d = min(digits)
                    max_d = max(digits)
                    if w2 > 0:
                        min_total += w2 * min_d
                        max_total += w2 * max_d
                    else:
                        min_total += w2 * max_d
                        max_total += w2 * min_d
                if not success:
                    assigned.pop(c)
                    used_digits[d] = False
                    continue
                if min_total <= 0 <= max_total:
                    if dfs(idx + 1, new_total):
                        return True
                assigned.pop(c)
                used_digits[d] = False
            return False

        return dfs(0, 0)
