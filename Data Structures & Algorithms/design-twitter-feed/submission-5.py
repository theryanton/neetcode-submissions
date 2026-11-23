class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list) # userId -> list of [count, tweetIds]
        self.followMap = defaultdict(set) # userid -> list of [following]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        if len(self.tweetMap[userId]) > 10:
            self.tweetMap[userId].pop(0)
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minheap = []
        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            tweets = self.tweetMap.get(followeeId)
            if tweets:
                idx = len(tweets) - 1
                count, tweetId = tweets[idx]
                heapq.heappush(minheap, (count, tweetId, followeeId, idx - 1))

        while minheap and len(res) < 10:
            _, tweetId, followeeId, idx = heapq.heappop(minheap)
            res.append(tweetId)
            if idx >= 0:
                count, nextTweetId = self.tweetMap[followeeId][idx]
                heapq.heappush(minheap, (count, nextTweetId, followeeId, idx - 1))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:    
            self.followMap[followerId].remove(followeeId)
