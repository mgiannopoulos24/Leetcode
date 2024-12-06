from collections import defaultdict
from bisect import bisect_left, bisect_right

class TweetCounts:

    def __init__(self):
        # Dictionary to store tweets by their name, each tweet name maps to a list of times
        self.tweet_map = defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        # Record the time for the given tweet name
        self.tweet_map[tweetName].append(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> list:
        # Determine the chunk size based on the frequency
        if freq == "minute":
            interval = 60
        elif freq == "hour":
            interval = 3600
        elif freq == "day":
            interval = 86400
        
        # Initialize result array to store tweet counts per chunk
        result = []
        
        # Get all the recorded tweet times for the given tweetName
        tweet_times = self.tweet_map[tweetName]
        
        # Sort the tweet times to make it easier to count in intervals
        tweet_times.sort()

        # Loop through the intervals from startTime to endTime
        for start in range(startTime, endTime + 1, interval):
            # Define the end of the current interval (make sure it doesn't exceed endTime)
            end = min(start + interval - 1, endTime)
            
            # Use binary search to efficiently count tweets within the range [start, end]
            left = bisect_left(tweet_times, start)
            right = bisect_right(tweet_times, end)
            
            # Append the count of tweets in this interval to the result
            result.append(right - left)
        
        return result


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)