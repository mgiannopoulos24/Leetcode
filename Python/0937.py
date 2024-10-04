from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # Separate the logs into letter-logs and digit-logs
        letter_logs = []
        digit_logs = []
        
        for log in logs:
            identifier, *content = log.split()
            if content[0].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append((identifier, ' '.join(content)))
        
        # Sort letter-logs by their content, and then by their identifier if contents are the same
        letter_logs.sort(key=lambda x: (x[1], x[0]))
        
        # Reconstruct the letter logs from tuples
        letter_logs = [f"{identifier} {content}" for identifier, content in letter_logs]
        
        # Concatenate sorted letter-logs with original digit-logs
        return letter_logs + digit_logs
