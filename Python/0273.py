class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        
        def number_to_words_below_1000(n: int) -> str:
            """Helper function to convert numbers less than 1000 to words"""
            if n == 0:
                return ""
            elif n < 20:
                return one_to_nineteen[n]
            elif n < 100:
                return tens[n // 10] + (" " + one_to_nineteen[n % 10] if n % 10 != 0 else "")
            else:
                return one_to_nineteen[n // 100] + " Hundred" + (" " + number_to_words_below_1000(n % 100) if n % 100 != 0 else "")
        
        def number_to_words(n: int) -> str:
            """Main function to convert number to words"""
            if n == 0:
                return "Zero"
            
            res = ""
            for i, chunk in enumerate(chunks):
                if n % 1000 != 0:
                    res = number_to_words_below_1000(n % 1000) + " " + chunk + (" " + res if res else "")
                n //= 1000
            return res.strip()
        
        # Define word representations for chunks
        chunks = ["", "Thousand", "Million", "Billion", "Trillion"]
        one_to_nineteen = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", 
                           "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", 
                           "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

        return number_to_words(num)
