class Solution:
    SIZE = 3

    # O(SIZE) time
    def checkRow(self, game: list, row: int) -> bool:
        # minVal = min(game[row][c] for c in range(self.SIZE))
        # maxVal = max(game[row][c] for c in range(self.SIZE))
        # return 0 < minVal == maxVal
        # HARDCODE FOR SPEED
        return 0 < game[row][0] == game[row][1] == game[row][2]


    # O(SIZE) time
    def checkCol(self, game: list, col: int) -> bool:
        # minVal = min(game[r][col] for r in range(self.SIZE))
        # maxVal = max(game[r][col] for r in range(self.SIZE))
        # return 0 < minVal == maxVal
        return 0 < game[0][col] == game[1][col] == game[2][col]


    # O(SIZE) time
    def checkDiag(self, game: list) -> bool:
        # minVal1 = min(game[x][x] for x in range(self.SIZE))
        # maxVal1 = max(game[x][x] for x in range(self.SIZE))
        # minVal2 = min(game[2 - x][x] for x in range(self.SIZE))
        # maxVal2 = max(game[2 - x][x] for x in range(self.SIZE))
        # return 0 < minVal1 == maxVal1 or 0 < minVal2 == maxVal2
        upperLeftLowerRight = 0 < game[0][0] == game[1][1] == game[2][2]
        lowerLeftUpperRight = 0 < game[2][0] == game[1][1] == game[0][2]
        return upperLeftLowerRight or lowerLeftUpperRight

    # O(SIZE^2) time
    def checkWinable(self, game: list) -> bool:
        for row in range(self.SIZE):
            oneInRow = False
            twoInRow = False
            for col in range(self.SIZE):
                oneInRow = oneInRow or game[row][col] == 1
                twoInRow = twoInRow or game[row][col] == 2
            if oneInRow != twoInRow and (oneInRow or twoInRow): return True

        for col in range(self.SIZE):
            oneInCol = False
            twoInCol = False
            for row in range(self.SIZE):
                oneInCol = oneInCol or game[row][col] == 1
                twoInCol = twoInCol or game[row][col] == 2
            if oneInCol != twoInCol and (oneInCol or twoInCol): return True

        # upper left to lower right
        oneInDiag = False
        twoinDiag = False
        for x in range(self.SIZE):
            oneInDiag = oneInDiag or game[x][x] == 1
            twoinDiag = twoinDiag or game[x][x] == 2
        if oneInDiag != twoinDiag and (oneInDiag or twoinDiag): return True

        # lower left to upper right
        oneInDiag = False
        twoinDiag = False
        for x in range(self.SIZE):
            oneInDiag = oneInDiag or game[2 - x][x] == 1
            twoinDiag = twoinDiag or game[2 - x][x] == 2
        if oneInDiag != twoinDiag and (oneInDiag or twoinDiag): return True

        return False


    # O(SIZE * n) time: n moves, checks take O(SIZE) each
    # O(SIZE^2) space: square board
    def tictactoe(self, moves: list) -> str:
        status = 'Pending'
        game = [[0] * self.SIZE for _ in range(self.SIZE)]

        for i, (r, c) in enumerate(moves):
            game[r][c] = i % 2 + 1
            if self.checkRow(game, r) \
            or self.checkCol(game, c) \
            or self.checkDiag(game): 
                status = 'A' if i % 2 == 0 else 'B'
                break

        # leetcode checks not recognizing unfinished games where no one can win as draw
        # if not self.checkWinable(game): status = 'Draw'
        if len(moves) == self.SIZE ** 2 and status == 'Pending': status = 'Draw'

        return status


testcases = [
    ([[0,0],[2,0],[1,1],[2,1],[2,2]], 'A'),
    ([[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]], 'B'),
    ([[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]], 'Draw'),
    ([[0,0],[1,1]], 'Pending'),
    ([[1,1],[2,0],[0,2],[0,1],[0,0],[2,2],[2,1],[1,2]], 'Pending'),
    ([[0,2],[1,0],[2,2],[1,2],[2,0],[0,0],[0,1],[2,1],[1,1]], 'A')
]

for i, (moves, target) in enumerate(testcases):
    output = Solution().tictactoe(moves)
    print('Case #{}: should be \'{}\', is \'{}\''.format(i + 1, target, output))
    assert target == output
print('All test cases passed!')