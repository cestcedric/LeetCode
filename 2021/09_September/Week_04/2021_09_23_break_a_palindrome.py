class Solution:
    # O(n) time: worst case = palindrome of all a, has to go to end
    # O(n) space: recursive call with half the palindrome
    # Can reduce space complexity by calling with indices instead of string
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) < 2: return ''

        def breaker(plndrm):
            if len(plndrm) == 0: return ''
            if len(plndrm) == 1: return 'a' if plndrm != 'a' else 'b'

            # prefix = all 'a' at beginning of word
            prefixIDX = 0
            while prefixIDX < len(plndrm) and plndrm[prefixIDX] == 'a': prefixIDX += 1
            
            if prefixIDX == len(plndrm): 
                return plndrm[:-1] + 'b'
            if prefixIDX == len(plndrm) // 2 and len(plndrm) % 2 == 1:
                return plndrm[:prefixIDX + 1] + breaker(plndrm[prefixIDX + 1:])
            return plndrm[:prefixIDX] + 'a' + plndrm[prefixIDX + 1:]

        return breaker(palindrome)


testcases = [
    ('abccba', 'aaccba'),
    ('a', ''),
    ('aa', 'ab'),
    ('bbbbb', 'abbbb'),
    ('aba', 'abb')
]

for i, (palindrome, target) in enumerate(testcases):
    output = Solution().breakPalindrome(palindrome)
    print('Case #{}: should be \'{}\', is \'{}\''.format(i + 1, target, output))
    assert target == output
print('All test cases passed!')