import random
import string

class Codec:
    def __init__(self):
        self.url_to_key = {}  # Maps long URL to a unique key
        self.key_to_url = {}  # Maps unique key to long URL
        self.base_url = "http://tinyurl.com/"
        self.key_length = 6  # Length of the unique key

    def generate_key(self) -> str:
        """Generate a unique key of fixed length."""
        return ''.join(random.choices(string.ascii_letters + string.digits, k=self.key_length))

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL."""
        if longUrl in self.url_to_key:
            key = self.url_to_key[longUrl]
        else:
            key = self.generate_key()
            while key in self.key_to_url:  # Ensure key is unique
                key = self.generate_key()
            self.url_to_key[longUrl] = key
            self.key_to_url[key] = longUrl
        return self.base_url + key

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL."""
        key = shortUrl.replace(self.base_url, '')
        return self.key_to_url.get(key, '')
        
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))