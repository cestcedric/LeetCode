from functools import lru_cache

class Solution:
    # O(k^n) time complexity: probably, really not sure in this case
    # O(k^n) space complexity: also probably
    @lru_cache()
    def generateParenthesis(self, n: int) -> list:
        if n == 0: return ['']
        if n == 1: return ['()']
        output = set()

        # X(X)X, X can be any valid sequence of parentheses
        for i in range(n):
            tmp1 = self.generateParenthesis(i)
            for j in range(n-i):
                tmp2 = self.generateParenthesis(j)
                tmp3 = self.generateParenthesis(n-1-i-j)
                tmp = [(t1, t2, t3) for t1 in tmp1 for t2 in tmp2 for t3 in tmp3]
                for t in tmp:
                    output.add('{}({}){}'.format(t[0], t[1], t[2]))

        return list(output)


testcases = [
    (4, ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]),
    (3, ['((()))','(()())','(())()','()(())','()()()']),
    (0, ['']),
    (2, ['(())', '()()']),
    (1, ['()'])
]

for i, (input, target) in enumerate(testcases):
    output = Solution().generateParenthesis(input)
    print('Case #{}; should be\n{}, is\n{}'.format(i+1, sorted(target), sorted(output)))
    print('-'*10)
    assert sorted(target) == sorted(output)
print('All test cases passed!')