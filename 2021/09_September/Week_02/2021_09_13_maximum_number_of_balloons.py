from collections import Counter

class Solution:
    # O(n) time
    # O(1) space
    def maxNumberOfBalloons(self, text: str) -> int:
        TARGET = 'balloon'
        counterTarget = Counter(TARGET)
        counterText = {c: 0 for c in TARGET}

        for t in text:
            if t in counterText:
                counterText[t] += 1

        return min(counterText[c] // counterTarget[c] for c in counterTarget)


testcases = [
    ('nlaebolko', 1),
    ('loonbalxballpoon', 2),
    ('leetcode', 0)
]

for i, (text, target) in enumerate(testcases):
    output = Solution().maxNumberOfBalloons(text)
    print('Case #{}: should be {}, is {}'.format(i + 1, target, output))
    assert target == output
print('All test cases passed!')