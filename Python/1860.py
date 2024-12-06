class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        time = 1
        while True:
            if memory1 >= memory2:
                if memory1 >= time:
                    memory1 -= time
                else:
                    return [time, memory1, memory2]
            else:
                if memory2 >= time:
                    memory2 -= time
                else:
                    return [time, memory1, memory2]
            time += 1
