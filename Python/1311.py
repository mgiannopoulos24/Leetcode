from collections import deque, Counter

class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        # BFS to find all friends at the given level
        n = len(friends)
        visited = [False] * n
        visited[id] = True
        
        # Start BFS
        queue = deque([id])
        current_level = 0
        
        while queue and current_level < level:
            for _ in range(len(queue)):
                person = queue.popleft()
                for friend in friends[person]:
                    if not visited[friend]:
                        visited[friend] = True
                        queue.append(friend)
            current_level += 1
        
        # Gather videos from friends at the required level
        video_count = Counter()
        for friend in queue:
            video_count.update(watchedVideos[friend])
        
        # Sort by frequency, and then alphabetically
        result = sorted(video_count.keys(), key=lambda x: (video_count[x], x))
        
        return result
