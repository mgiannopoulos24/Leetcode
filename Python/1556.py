class Solution:
    def thousandSeparator(self, n: int) -> str:
        # Format the number using commas as thousands separators, then replace commas with dots
        return "{:,}".format(n).replace(',', '.')
