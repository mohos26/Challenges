# https://leetcode.com/problems/gas-station
# 24/05/2026


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
