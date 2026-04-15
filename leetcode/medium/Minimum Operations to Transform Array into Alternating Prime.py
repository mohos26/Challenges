# https://leetcode.com/problems/minimum-operations-to-transform-array-into-alternating-prime/
# 11.04.2026


class Solution:
    def is_prime(self, num):
        if num < 2: return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def extended_sieve(self, n):
        n_is_prime = self.is_prime(n)

        limit = n
        found_target = False

        while not found_target:
            limit += 1
            current_is_prime = self.is_prime(limit)

            if n_is_prime != current_is_prime:
                found_target = True

        prime_flags = [True] * (limit + 1)
        prime_flags[0] = prime_flags[1] = False

        for p in range(2, int(limit**0.5) + 1):
            if prime_flags[p]:
                for i in range(p * p, limit + 1, p):
                    prime_flags[i] = False

        primes_list = [num for num, is_p in enumerate(prime_flags) if is_p]
        non_primes_list = [num for num, is_p in enumerate(prime_flags) if not is_p]

        return primes_list, non_primes_list

    def minOperations(self, nums: list[int]) -> int:
        res = 0
        primes_list, non_primes_list = self.extended_sieve(max(nums))
        primes_set = set(primes_list)
        for i, n in enumerate(nums):
            is_prime = n in primes_set
            if i % 2:
                if is_prime:
                    res += abs(n - non_primes_list[bisect_right(non_primes_list, n)])
            else:
                if not is_prime:
                    res += abs(n - primes_list[bisect_right(primes_list, n)])
        return res

