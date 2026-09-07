from typing import List
import heapq

class Twitter:
    def __init__(self):
        self.following = {}
        self.user = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId in self.user:
            self.user[userId].append((self.time, tweetId))
        else:
            self.user[userId] = [(self.time, tweetId)]
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        ids = self.following.get(userId, set()) | {userId}
        heap = []
        for friend in ids:
            if friend in self.user:
                for time, tweetId in self.user[friend]:
                    heapq.heappush(heap, (time, tweetId))
                    if len(heap) > 10:
                        heapq.heappop(heap)
        result = []
        while heap:
            result.append(heapq.heappop(heap)[1])
        return result[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].add(followeeId)
        else:
            self.following[followerId] = set([followeeId])

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].discard(followeeId)
