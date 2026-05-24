# https://leetcode.com/problems/gas-station
# 24.05.2026


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        last = -1
        i = 0
        while last < i:
            tank = 0
            last = i
            for _ in range(n):
                tank += gas[i] - cost[i]
                if tank < 0:
                    break
                i = (i + 1) % n
            else:
                return i
            i = (i + 1) % n
        return -1


# 24.05.2026
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        res = None
        total = 0
        for i, arg in enumerate(zip(gas, cost)):
            total += arg[0] - arg[1]
            if total < 0:
                total = 0
                res = None
            elif res is None:
                res = i
        return res
