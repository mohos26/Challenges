# https://leetcode.com/problems/ugly-number
# 27.11.2025


import numpy as np

class Solution_Wrong: # Time out but it a good method
    def ft_aid(self, n):
        return n > 2 and not any([not n % num for num in self.allow_primes])

    def isUgly(self, n: int) -> bool: # Sieve of Eratosthenes
        self.allow_primes = 2, 3, 5
        if n <= 0 or self.ft_aid(n):
            return False
        lst = np.zeros(n+1, dtype=bool)
        for num in range(2, n):
            if lst[num]:
                continue
            if not n % num and num not in self.allow_primes:
                return False
            for i in range(num, n, num):lst[i] = True
        return True


class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        while n != 1:
            if not n % 2:
                while not n % 2:
                    n //= 2
            elif not n % 3:
                while not n % 3:
                    n //= 3
            elif not n % 5:
                while not n % 5:
                    n //= 5
            else:
                return False
        return True

