class Solution:
    # O(n) time: leaf nodes are immediately collapsed when identified
    # O(h) space: height of binary tree, worst case O(n)
    def isValidSerialization(self, preorder: str) -> bool:
        preorder = preorder.split(',')
        stack = []

        def isLeaf(stack: list) -> bool:
            return stack[-3] != '#' and stack[-2] == stack[-1] == '#'

        def popLeaf(stack: list) -> None:
            for _ in range(3): stack.pop()
            stack.append('#')

        for p in preorder:
            stack.append(p)
            while len(stack) > 2 and isLeaf(stack):
                popLeaf(stack)
        
        return stack == ['#']




testcases = [
    ('9,3,4,#,#,1,#,#,2,#,6,#,#', True),
    ('1,#', False),
    ('9,#,#,1', False),
    ('9,#,1,#', False),
    ('9,#,92,#,#', True)
]

for i, (preorder, target) in enumerate(testcases):
    output = Solution().isValidSerialization(preorder)
    print('Case #{}: should be {}, is {}'.format(i + 1, target, output))
    assert target == output
print('All test cases passed!')