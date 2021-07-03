class Solution:
    # O(2^n) time complexity: n => upper limit 2^n - 1 => 2^n calls
    # O(2^n) space complexity: call stack
    def grayCode(self, n: int) -> list:
        
        def rec(n):
            if n == 1: return ['0', '1']
            prev = rec(n - 1)
            left = ['0' + b for b in prev]
            right = ['1' + b for b in prev[::-1]]
            return left + right

        return [int(b, 2) for b in rec(n)]

    
    def grayCodeIT(self, n: int) -> list:
        tmp = ['0', '1']

        for _ in range(1, n):
            left = ['0' + b for b in tmp]
            right = ['1' + b for b in tmp[::-1]]
            tmp = left + right

        return [int(b, 2) for b in tmp]
        


testcases = [
    (2, [[0,1,3,2], [0,2,3,1]]),
    (1, [[0,1]])
]

for i, (input, target) in enumerate(testcases):
    output = Solution().grayCode(input)
    print('Case #{} solved: {}'.format(i+1, output in target))
    assert output in target
print('All test cases passed!')

