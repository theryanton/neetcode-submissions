class Twitter:

    def __init__(self):
        self.count = 0
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        if len(self.tweetMap[userId]) > 10:
            self.tweetMap[userId].pop(0)
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        minheap = []

        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            tweets = self.tweetMap[followeeId]
            if tweets:
                index = len(tweets) - 1
                count, tweetId = tweets[index]
                heapq.heappush(minheap, [count, tweetId, followeeId, index - 1])
        
        res = []
        while minheap and len(res) < 10:
            count, tweetId, followeeId, nextIndex = heapq.heappop(minheap)
            res.append(tweetId)
            if nextIndex >= 0:
                count, tweetId = self.tweetMap[followeeId][nextIndex]
                heapq.heappush(minheap, [count, tweetId, followeeId, nextIndex - 1])
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
