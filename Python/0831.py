class Solution:
    def maskPII(self, s: str) -> str:
        # Check if the input is an email by looking for the '@' symbol
        if '@' in s:
            # Email processing
            local, domain = s.split('@')
            local = local.lower()
            domain = domain.lower()
            # Mask the local part of the email
            masked_email = local[0] + "*****" + local[-1] + "@" + domain
            return masked_email
        else:
            # Phone number processing
            digits = [c for c in s if c.isdigit()]  # Extract digits from the input string
            local_number = ''.join(digits[-10:])    # The last 10 digits are the local number
            country_code = digits[:-10]             # The remaining digits form the country code
            
            masked_local = "***-***-" + local_number[-4:]
            if len(country_code) == 0:
                return masked_local
            else:
                # Construct the masked phone number with the country code
                return "+" + "*" * len(country_code) + "-" + masked_local
