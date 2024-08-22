function longestPalindrome(s: string): string {
    if (s.length === 0) return "";

    let start = 0;
    let maxLen = 1;

    const expandAroundCenter = (left: number, right: number): [number, number] => {
        while (left >= 0 && right < s.length && s[left] === s[right]) {
            left--;
            right++;
        }
        return [left + 1, right];
    };

    for (let i = 0; i < s.length; i++) {
        // Odd-length palindromes (centered at i)
        const [l1, r1] = expandAroundCenter(i, i);
        // Even-length palindromes (centered between i and i + 1)
        const [l2, r2] = expandAroundCenter(i, i + 1);

        // Update maximum length palindrome if necessary
        if (r1 - l1 > maxLen) {
            start = l1;
            maxLen = r1 - l1;
        }
        if (r2 - l2 > maxLen) {
            start = l2;
            maxLen = r2 - l2;
        }
    }

    return s.substring(start, start + maxLen);
}