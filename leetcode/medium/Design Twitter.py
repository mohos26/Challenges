# https://leetcode.com/problems/design-twitter/
# 03.01.2026



class Twitter: # heap
    def __init__(self):
        # key: id of user; value: [tweets, followers]; tweets: [time, tweet id]
        self.d = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.initialize(userId)
        self.d[userId][0].append((self.getime(), tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        self.initialize(userId)
        heap = list(self.d[userId][0])
        heapq.heapify(heap)
        for _id in self.d[userId][1]:
            self.initialize(_id)
            for tweet in self.d[_id][0]:
                if len(heap) == 10:
                    heapq.heappushpop(heap, tweet)
                else:
                    heapq.heappush(heap, tweet)
        res = [heapq.heappop(heap)[1] for _ in range(min(len(heap), 10))]
        res.reverse()
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.initialize(followerId)
        if followeeId not in self.d[followerId][1]:
            self.d[followerId][1].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.initialize(followerId)
        if followeeId in self.d[followerId][1]:
            self.d[followerId][1].remove(followeeId)

    def getime(self):
        self.time += 1
        return self.time

    def initialize(self, userId):
        if userId not in self.d:
            self.d[userId] = deque(maxlen=10), []


class Twitter_2: # sorted list
    def __init__(self):
        # key: id of user; value: [tweets, followers]; tweets: [time, tweet id]
        self.d = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.initialize(userId)
        self.d[userId][0].append((self.getime(), tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        self.initialize(userId)
        lst = list(self.d[userId][0])
        for _id in self.d[userId][1]:
            self.initialize(_id)
            for tweet in self.d[_id][0]:
                bisect.insort(lst, tweet)
                if len(lst) > 10:
                    lst.pop(0)
        lst.reverse()
        return [b for a, b in lst]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.initialize(followerId)
        if followeeId not in self.d[followerId][1]:
            self.d[followerId][1].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.initialize(followerId)
        if followeeId in self.d[followerId][1]:
            self.d[followerId][1].remove(followeeId)

    def getime(self):
        self.time += 1
        return self.time

    def initialize(self, userId):
        if userId not in self.d:
            self.d[userId] = deque(maxlen=10), []

