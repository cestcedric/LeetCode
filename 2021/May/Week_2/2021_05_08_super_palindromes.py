from   itertools import count
import math

class Solution:
    def getPalindrome(self, minDigits, maxDigits):
        # https://stackoverflow.com/a/19857182
        yield 0
        for digits in range(minDigits, maxDigits):
            first = 10 ** ((digits - 1) // 2)
            for s in map(str, range(first, 10 * first)):
                yield int(s + s[-(digits % 2)-1::-1])


    def superpalindromesInRange(self, left: str, right: str) -> int:
        left_i = int(left)
        right_i = int(right)

        left_sqrt = math.ceil(math.sqrt(left_i))
        right_sqrt = math.floor(math.sqrt(right_i))

        gen = self.getPalindrome(len(str(left_sqrt)), len(str(right_sqrt)) + 1)
        
        palindromes = 0
        for p in gen:
            if p < left_sqrt:
                continue
            if p > right_sqrt:
                return palindromes
            square = str(p**2)
            palindromes += (square == square[::-1])
        return palindromes


testcases = [
    ('4', '1000', 4),
    ('1', '2', 1),
    ('3', '12', 2)
]

for left, right, t in testcases:
    r = Solution().superpalindromesInRange(left, right)
    print('Left: {}, right: {}, super palindromes: {}. Your result: {}.'.format(left, right, t, r))
    assert r == t