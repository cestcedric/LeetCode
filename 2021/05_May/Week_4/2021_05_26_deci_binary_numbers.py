class Solution:
    def minPartitions(self, n: str) -> int:
        return int(max(n))


testcases = [
    ('32', 3),
    ('82734', 8),
    ('27346209830709182346', 9)
]

for i, (input, target) in enumerate(testcases):
    output = Solution().minPartitions(input)
    print('Case #{} should be {}, is {}'.format(i+1, target, output))
    assert target == output

print('All test cases passed!')
