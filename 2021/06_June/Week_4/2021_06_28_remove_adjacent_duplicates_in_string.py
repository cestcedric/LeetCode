class Solution:
    # O(n) time complexity: one pass through input string
    # O(n) space complexity: stack contains at most the complete string
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for c in s:
            if stack == [] or stack[-1] != c: stack.append(c)
            else: stack.pop()
        return ''.join(stack)

    # O(n*r) time complexity: at most n/2 duplicate pairs, O(r) time complexity for replace
    # O(1) space complexity: working on original string
    def removeDuplicatesIt(self, s: str) -> str:
        candidates = [c*2 for c in set(s)]
        prevLength = -1
        
        while prevLength != len(s):
            prevLength = len(s)
            for c in candidates:
                s = s.replace(c, '')

        return s


testcases = [
    ('abbaca', 'ca'),
    ('azxxzy', 'ay')
]

for i, (input, target) in enumerate(testcases):
    output = Solution().removeDuplicates(input)
    print('Case #{}: should be {}, is {}'.format(i + 1, target, output))
    assert target == output
print('All test cases passed!')