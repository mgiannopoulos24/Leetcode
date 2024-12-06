class BrowserHistory:

    def __init__(self, homepage: str):
        # Initialize the history with the homepage
        self.history = [homepage]
        self.current = 0  # Points to the current URL
        self.last = 0     # Points to the last URL, clearing forward history when visiting

    def visit(self, url: str) -> None:
        # Visit a new URL, clearing any forward history
        self.current += 1
        if self.current < len(self.history):
            self.history[self.current] = url
        else:
            self.history.append(url)
        self.last = self.current  # Reset the last pointer to the current
        

    def back(self, steps: int) -> str:
        # Move back by steps, but not beyond index 0
        self.current = max(0, self.current - steps)
        return self.history[self.current]

    def forward(self, steps: int) -> str:
        # Move forward by steps, but not beyond the last valid index
        self.current = min(self.last, self.current + steps)
        return self.history[self.current]

        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)