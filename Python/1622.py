MOD = 10**9 + 7

class Fancy:

    def __init__(self):
        self.seq = []
        self.add_factor = 0
        self.mult_factor = 1

    def append(self, val: int) -> None:
        # Store the value adjusted by the current mult_factor and add_factor
        adjusted_val = (val - self.add_factor + MOD) * pow(self.mult_factor, MOD - 2, MOD) % MOD
        self.seq.append(adjusted_val)

    def addAll(self, inc: int) -> None:
        # Only modify the add_factor
        self.add_factor = (self.add_factor + inc) % MOD

    def multAll(self, m: int) -> None:
        # Multiply both the mult_factor and the add_factor
        self.mult_factor = self.mult_factor * m % MOD
        # Since we apply multiplication to the entire sequence, the previous additions also need to be multiplied
        self.add_factor = self.add_factor * m % MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.seq):
            return -1
        # Calculate the actual value considering the transformations
        return (self.seq[idx] * self.mult_factor + self.add_factor) % MOD


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)