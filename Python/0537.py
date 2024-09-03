class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        def parse_complex_number(s: str) -> tuple:
            real, imaginary = s.split('+')
            imaginary = imaginary[:-1]  # Remove the trailing 'i'
            return int(real), int(imaginary)

        # Parse both complex numbers
        a, b = parse_complex_number(num1)
        c, d = parse_complex_number(num2)
        
        # Calculate the real and imaginary parts of the product
        real_part = a * c - b * d
        imaginary_part = a * d + b * c
        
        # Format the result as a string
        return f"{real_part}+{imaginary_part}i"
