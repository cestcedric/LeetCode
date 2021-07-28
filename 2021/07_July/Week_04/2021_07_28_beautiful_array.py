from functools import lru_cache

class Solution:
    # O(n) time complexity: log(n) levels of recursion, each of size n / 2
    # O(n) space complexity: same argument as for time complexity
    @lru_cache(None)
    def beautifulArray(self, n: int) -> list:
        if n == 1: return [1]
        
        odd = self.beautifulArray(n // 2) if n % 2 == 0 else self.beautifulArray(n // 2 + 1)
        even = self.beautifulArray(n // 2)

        output = [o * 2 - 1 for o in odd] + [e * 2 for e in even]
        return output


print(Solution().beautifulArray(8))

