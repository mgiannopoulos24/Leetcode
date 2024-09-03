class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def is_valid_ipv4(ipv4: str) -> bool:
            parts = ipv4.split('.')
            if len(parts) != 4:
                return False
            for part in parts:
                if not part.isdigit():
                    return False
                num = int(part)
                if num < 0 or num > 255:
                    return False
                if part != str(num):  # No leading zeros
                    return False
            return True

        def is_valid_ipv6(ipv6: str) -> bool:
            parts = ipv6.split(':')
            if len(parts) != 8:
                return False
            for part in parts:
                if not (1 <= len(part) <= 4):
                    return False
                if not all(c in "0123456789abcdefABCDEF" for c in part):
                    return False
            return True

        if '.' in queryIP and ':' in queryIP:
            return "Neither"
        if '.' in queryIP:
            return "IPv4" if is_valid_ipv4(queryIP) else "Neither"
        if ':' in queryIP:
            return "IPv6" if is_valid_ipv6(queryIP) else "Neither"
        return "Neither"
