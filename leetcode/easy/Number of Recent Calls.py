# https://leetcode.com/problems/number-of-recent-calls/
# 14.08.2026


class RecentCounter:
    def __init__(self):
        self.d = deque()

    def ping(self, t: int) -> int:
        while self.d:
            if t - self.d[0] > 3000:
                self.d.popleft()
            else:
                break
        self.d.append(t)
        return len(self.d)

