class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        result = [0] * n  # To store the exclusive time of each function
        stack = []  # Stack to keep track of the function calls (function_id, start_time)
        prev_time = 0  # Previous timestamp
        
        for log in logs:
            function_id, action, timestamp = log.split(":")
            function_id, timestamp = int(function_id), int(timestamp)
            
            if action == "start":
                # If there's a function running, update its time with the time spent since prev_time
                if stack:
                    result[stack[-1]] += timestamp - prev_time
                # Push the current function to the stack
                stack.append(function_id)
                prev_time = timestamp
            else:  # action == "end"
                # Pop the current function from the stack and update its exclusive time
                result[stack.pop()] += timestamp - prev_time + 1
                # Update prev_time for the next iteration
                prev_time = timestamp + 1
        
        return result
