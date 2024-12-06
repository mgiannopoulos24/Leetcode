class AuthenticationManager:
    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive  # Time to live for each token
        self.tokens = {}  # Dictionary to store tokens with their expiration times

    def generate(self, tokenId: str, currentTime: int) -> None:
        # Generate a new token with expiration time
        self.tokens[tokenId] = currentTime + self.timeToLive

    def renew(self, tokenId: str, currentTime: int) -> None:
        # Renew the token only if it's unexpired
        if tokenId in self.tokens and self.tokens[tokenId] > currentTime:
            self.tokens[tokenId] = currentTime + self.timeToLive

    def countUnexpiredTokens(self, currentTime: int) -> int:
        # Count tokens that are unexpired
        return sum(1 for expire_time in self.tokens.values() if expire_time > currentTime)


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)