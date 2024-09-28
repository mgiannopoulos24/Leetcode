class Solution:
    def isValid(self, code: str) -> bool:
        n = len(code)
        stack = []
        i = 0

        if not code:
            return False

        while i < n:
            if code[i] != '<':
                if not stack:
                    # All content must be inside a tag
                    return False
                i += 1
                continue

            # Check if it's a CDATA section
            if i + 9 <= n and code[i:i+9] == "<![CDATA[":
                if not stack:
                    return False
                j = i + 9
                # Find the next "]]>"
                close = code.find("]]>", j)
                if close == -1:
                    return False
                i = close + 3
                continue

            # Check if it's an end tag
            if i + 2 <= n and code[i+1] == '/':
                j = code.find('>', i)
                if j == -1:
                    return False
                tagname = code[i+2:j]
                if not stack or stack[-1] != tagname:
                    return False
                stack.pop()
                i = j + 1
                if not stack and i != n:
                    # After the outermost tag is closed, there should be nothing else
                    return False
                continue

            # It's a start tag
            j = code.find('>', i)
            if j == -1:
                return False
            tagname = code[i+1:j]

            # Check if the tag contains invalid characters (like '<', '>', or spaces)
            if '<' in tagname or '>' in tagname or ' ' in tagname:
                return False

            # Ensure tagname is valid: length between 1 and 9, and all uppercase letters
            if not 1 <= len(tagname) <= 9 or not tagname.isupper():
                return False
            stack.append(tagname)
            i = j + 1
            continue

        return not stack
