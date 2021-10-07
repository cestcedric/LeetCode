class Solution:
    # O(m*n*3^k) time: DFS in 3 possible directions
    # O(m*n) space: visited set
    # can be reduced to O(1) by setting visited entries to None and
    # resetting them to the original entry on the way back
    def exist(self, board: list, word: str) -> bool:
        m, n = len(board), len(board[0])

        visited = set()

        def getNeighbors(r, c):
            nonlocal m, n
            neighbors = []

            if r > 0: neighbors.append((r - 1, c))
            if r < m - 1: neighbors.append((r + 1, c))
            if c > 0: neighbors.append((r, c - 1))
            if c < n - 1: neighbors.append((r, c + 1))

            return neighbors

        def dfs(r, c, i):
            nonlocal board, word, visited

            if board[r][c] != word[i]: return False
            if (r, c) in visited: return False
            if i == len(word) - 1: return True

            visited.add((r, c))

            for new_r, new_c in getNeighbors(r, c):
                if dfs(new_r, new_c, i + 1): return True

            visited.remove((r, c))
            
            return False

        for r in range(m):
            for c in range(n):
                if dfs(r, c, 0): return True
        
        return False



testcases = [
    ([['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], 'ABCCED', True),
    ([['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], 'SEE', True),
    ([['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], 'ABCD', False),
    ([['A']], 'A', True),
    ([['A','B','C','E'],['S','F','E','S'],['A','D','E','E']], 'ABCESEEEFS', True)
]

for i, (board, word, target) in enumerate(testcases):
    output = Solution().exist(board, word)
    print('Case #{}: should be {}, is {}'.format(i + 1, target, output))
    assert target == output
print('All test cases passed!')
        