from string import ascii_lowercase

class Solution:
    # O(n) time
    # O(1) space
    def shiftingLetters(self, s: str, shifts: list) -> str:

        numToChar = {i: c for i, c in enumerate(ascii_lowercase)}
        charToNum = {c: i for i, c in enumerate(ascii_lowercase)}

        output = ''
        totalShift = 0
        for c, shift in zip(s[::-1], shifts[::-1]):
            totalShift += shift
            num = charToNum[c] + totalShift
            num %= 26
            output += numToChar[num]

        return output[::-1]


testcases = [
    ('abc', [3,5,9], 'rpl'),
    ('aaa', [1,2,3], 'gfd')
]

for i, (s, shifts, target) in enumerate(testcases):
    output = Solution().shiftingLetters(s, shifts)
    print('Case #{}: should be \'{}\', is \'{}\''.format(i + 1, target, output))
    assert target == output
print('All test cases passed!')