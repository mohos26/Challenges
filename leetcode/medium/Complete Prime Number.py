# https://leetcode.com/problems/complete-prime-number/
# 09.12.2025


class Solution:
    def is_prime(self, n):
        if n < 2:
            return False
        for i in range(2, floor(sqrt(n)) + 1):
            if not n % i:
                return False
        return True


    def completePrime(self, num: int) -> bool:
        for i in range(floor(log10(num)), -1, -1):
            if not self.is_prime(num // 10**i):
                return False
        for i in range(1, floor(log10(num)) + 1):
            if not self.is_prime(num % 10**i):
                return False
        return True

