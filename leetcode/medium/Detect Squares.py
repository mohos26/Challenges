# https://leetcode.com/problems/detect-squares
# 03.07.2026


class DetectSquares:
    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points[tuple(map(float, point))] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        ax, ay = tuple(map(float, point))
        for (dx, dy) in self.points:
            if dx == ax or dy == ay or abs(dx - ax) != abs(dy - ay):
                continue
            mx, my = round((ax + dx) / 2, 6), round((ay + dy) / 2, 6)
            amx, amy = mx - ax, my - ay
            b = mx - amx, my + amy
            c = mx + amx, my - amy
            if c in self.points and b in self.points:
                res += self.points[(dx, dy)] * self.points[b] * self.points[c]
        return res

