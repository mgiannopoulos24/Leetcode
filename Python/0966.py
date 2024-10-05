class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def canonical_form(word: str) -> str:
            vowels = set('aeiou')
            return ''.join(c if c not in vowels else '*' for c in word.lower())
        
        # Maps for lookups
        exact_match = {}
        case_insensitive_match = {}
        vowel_error_match = {}
        
        # Populate exact_match and case_insensitive_match
        for word in wordlist:
            lower_word = word.lower()
            if lower_word not in case_insensitive_match:
                case_insensitive_match[lower_word] = word
            if word not in exact_match:
                exact_match[word] = word
        
        # Populate vowel_error_match
        for word in wordlist:
            canonical = canonical_form(word)
            if canonical not in vowel_error_match:
                vowel_error_match[canonical] = word
        
        results = []
        
        for query in queries:
            if query in exact_match:
                results.append(exact_match[query])
            elif query.lower() in case_insensitive_match:
                results.append(case_insensitive_match[query.lower()])
            else:
                canonical_query = canonical_form(query)
                if canonical_query in vowel_error_match:
                    results.append(vowel_error_match[canonical_query])
                else:
                    results.append("")
        
        return results
