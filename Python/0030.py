class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words or not words[0]:
            return []

        word_length = len(words[0])
        num_words = len(words)
        substring_length = word_length * num_words
        word_count = Counter(words)
        result = []

        for i in range(word_length):
            left = i
            right = i
            current_count = defaultdict(int)
            while right + word_length <= len(s):
                word = s[right:right + word_length]
                right += word_length
                if word in word_count:
                    current_count[word] += 1
                    while current_count[word] > word_count[word]:
                        current_count[s[left:left + word_length]] -= 1
                        left += word_length
                    if right - left == substring_length:
                        result.append(left)
                else:
                    current_count.clear()
                    left = right

        return result