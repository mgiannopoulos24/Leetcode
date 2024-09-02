from collections import defaultdict
import heapq
from typing import List

class Twitter:
    def __init__(self):
        # Store tweets as a dictionary: user_id -> list of (timestamp, tweet_id)
        self.tweets = defaultdict(list)
        # Store following relationships as a dictionary: user_id -> set of followed_user_ids
        self.following = defaultdict(set)
        # Initialize a global timestamp
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Increase the timestamp to ensure correct tweet ordering
        self.timestamp += 1
        # Append the tweet with its timestamp
        self.tweets[userId].append((self.timestamp, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        # Create a max heap (simulated using negative timestamps)
        max_heap = []
        
        # Add tweets from the user itself
        if userId in self.tweets:
            for tweet in self.tweets[userId]:
                heapq.heappush(max_heap, (-tweet[0], tweet[1]))
        
        # Add tweets from the users the current user is following
        for followeeId in self.following[userId]:
            if followeeId in self.tweets:
                for tweet in self.tweets[followeeId]:
                    heapq.heappush(max_heap, (-tweet[0], tweet[1]))
        
        # Extract the 10 most recent tweets
        recent_tweets = []
        while max_heap and len(recent_tweets) < 10:
            _, tweetId = heapq.heappop(max_heap)
            recent_tweets.append(tweetId)
        
        return recent_tweets

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
