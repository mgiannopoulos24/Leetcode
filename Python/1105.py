class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        dp = [float('inf')] * (n + 1)  # dp[i] stores the minimum height after placing the first i books
        dp[0] = 0  # No books, no height

        # Loop over each book
        for i in range(1, n + 1):
            width = 0
            max_height = 0
            # Try placing books j to i on the same shelf
            for j in range(i, 0, -1):
                width += books[j-1][0]  # Add the thickness of book j-1
                if width > shelfWidth:  # If width exceeds, stop
                    break
                max_height = max(max_height, books[j-1][1])  # Find the max height on the shelf
                dp[i] = min(dp[i], dp[j-1] + max_height)  # Update the minimum height

        return dp[n]
