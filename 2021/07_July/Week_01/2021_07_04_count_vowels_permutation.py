from functools import lru_cache

class Solution:
    # O(n) time complexity: 5 * O(n - 1) function calls
    # O(n) space complexity: caching and callstack
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10 ** 9 + 7

        @lru_cache(None)
        def buildRec(n, prev = ''):
            nonlocal MOD
            if n == 0: return 1
            if prev == 'a': 
                return buildRec(n - 1, 'e')
            if prev == 'e': 
                return (buildRec(n - 1, 'a') + buildRec(n - 1, 'i')) % MOD
            if prev == 'i':
                return (buildRec(n - 1, 'a') + \
                        buildRec(n - 1, 'e') + \
                        buildRec(n - 1, 'o') + \
                        buildRec(n - 1, 'u')) % MOD
            if prev == 'o':
                return (buildRec(n - 1, 'i') + buildRec(n - 1, 'u')) % MOD
            if prev == 'u': 
                return buildRec(n - 1, 'a')
            
            return (buildRec(n - 1, 'a') + \
                    buildRec(n - 1, 'e') + \
                    buildRec(n - 1, 'i') + \
                    buildRec(n - 1, 'o') + \
                    buildRec(n - 1, 'u')) % MOD

        return buildRec(n, prev = '')


testcases = [
    (1, 5),
    (2, 10),
    (5, 68)
]

for i, (input, target) in enumerate(testcases):
    output = Solution().countVowelPermutation(input)
    print('Case #{}: should be {}, is {}'.format(i + 1, target, output))
    assert target == output
print('All test cases passed!')