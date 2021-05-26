class Solution:
    def toLowerCase(self, s: str) -> str:
        # O(n) time and space complexity
        return ''.join([ chr(ord(c) + 32) if ord(c) > 64  and ord(c) < 91 else c for c in s ])



testcases = [
    ('Hallo', 'hallo'),
    ('', ''),
    ('test123', 'test123')
]

for i, (s, result) in enumerate(testcases):
    res = Solution().toLowerCase(s)
    print('Case #{}: should be \'{}\', is \'{}\''.format(i+1, result, res))
    assert res == result
print('All test cases passed!')
        