class Solution:
    def entityParser(self, text: str) -> str:
        # Dictionary mapping of HTML entities to corresponding characters
        html_entities = {
            "&quot;": "\"",
            "&apos;": "'",
            "&gt;": ">",
            "&lt;": "<",
            "&frasl;": "/",
            "&amp;": "&"
        }
        
        # Iterate through the dictionary and replace all occurrences in the text
        # Replace more specific entities (like &gt;) before general ones (like &amp;)
        for entity, char in html_entities.items():
            text = text.replace(entity, char)
        
        return text