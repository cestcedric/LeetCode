class Solution:
    # O(n^2) time: n^2 entries in grid
    # -> each direction computed in constant time
    # -> overall possible cross size in constant time
    # O(n^2) space: still n^2 entries in grid
    def orderOfLargestPlusSign(self, n: int, mines: list) -> int:
        mines = {tuple(mine) for mine in mines}

        left = [[0] * n for _ in range(n)]
        right = [[0] * n for _ in range(n)]
        top = [[0] * n for _ in range(n)]
        bottom = [[0] * n for _ in range(n)]

        # left -> right
        for x in range(n):
            count = 0
            for y in range(n):
                if (x, y) in mines: count = 0
                else: count += 1
                left[x][y] = count

        # right -> left
        for x in range(n):
            count = 0
            for y in range(n - 1, -1, -1):
                if (x, y) in mines: count = 0
                else: count += 1
                right[x][y] = count

        # top -> bottom
        for y in range(n):
            count = 0
            for x in range(n):
                if (x, y) in mines: count = 0
                else: count += 1
                top[x][y] = count

        # bottom -> top
        for y in range(n):
            count = 0
            for x in range(n - 1, -1, -1):
                if (x, y) in mines: count = 0
                else: count += 1
                bottom[x][y] = count

        maxCross = 0

        for x in range(n):
            for y in range(n):
                maxCross = max(maxCross, min(left[x][y], right[x][y], top[x][y], bottom[x][y]))
        
        return maxCross


testcases = [
    (5, [[4,2]], 2),
    (1, [[0,0]], 0)
]

for i, (n, mines, target) in enumerate(testcases):
    output = Solution().orderOfLargestPlusSign(n, mines)
    print('Case #{}: should be {}, is {}'.format(i + 1, target, output))
    assert target == output
print('All test cases passed')