class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        def backtrack(index, sequence):
            if index == len(num):
                return len(sequence) >= 3
            current_num = 0
            for i in range(index, len(num)):
                if i > index and num[index] == '0':
                    break  # Leading zero is not allowed
                current_num = current_num * 10 + int(num[i])
                if current_num > 2**31 - 1:
                    break  # Number exceeds the limit
                if len(sequence) < 2 or sequence[-2] + sequence[-1] == current_num:
                    sequence.append(current_num)
                    if backtrack(i + 1, sequence):
                        return True
                    sequence.pop()
                elif len(sequence) >= 2 and sequence[-2] + sequence[-1] < current_num:
                    break
            return False
        
        sequence = []
        backtrack(0, sequence)
        return sequence if len(sequence) >= 3 else []