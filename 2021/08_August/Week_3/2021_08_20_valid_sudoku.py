class Solution:
    BOARDSIZE = 9
    SUBGRID = 3

    # O(n) time, O(n) space
    def checkRow(self, board: list, row: int) -> bool:
        entries = set()
        for col in range(self.BOARDSIZE):
            if board[row][col] == '.': continue
            if board[row][col] in entries: 
                return False
            entries.add(board[row][col])
        return True

    # O(n) time, O(n) space
    def checkCol(self, board: list, col: int) -> bool:
        entries = set()
        for row in range(self.BOARDSIZE):
            if board[row][col] == '.': continue
            if board[row][col] in entries: 
                return False
            entries.add(board[row][col])
        return True


    # O(n) time, O(BOARDSIZE) space
    def checkBlock(self, board: list, blockCenterRow: int, blockCenterCol: int) -> bool:
        entries = set()

        blockEntries = [s for s in range(-self.SUBGRID // 2 + 1, self.SUBGRID // 2 + 1)]
        for i in blockEntries:
            for j in blockEntries:
                if board[blockCenterRow + i][blockCenterCol + j] == '.': continue
                if board[blockCenterRow + i][blockCenterCol + j] in entries: 
                    return False
                entries.add(board[blockCenterRow + i][blockCenterCol + j])
        
        return True
        

    # O(n^2) time: check all entries three times
    # O(n) space: all entries in n x n Sudoku between 1 and n
    def isValidSudoku(self, board: list) -> bool:
        # check rows
        for row in range(self.BOARDSIZE):
            if not self.checkRow(board, row): 
                return False

        # check cols
        for col in range(self.BOARDSIZE):
            if not self.checkCol(board, col): 
                return False

        # check blocks
        for row in range(self.BOARDSIZE // self.SUBGRID):
            for col in range(self.BOARDSIZE // self.SUBGRID):
                blockCenterRow = row * 3 + 1
                blockCenterCol = col * 3 + 1
                if not self.checkBlock(board, blockCenterRow, blockCenterCol):
                    return False

        return True


testcases = [
    (
        [["8","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]],
        False
    ),
    (
        [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]],
        True
    )
]

for i, (board, target) in enumerate(testcases):
    output = Solution().isValidSudoku(board)
    print('Case #{}: should be {}, is {}'.format(i + 1, target, output))
    assert target == output
print('All test cases passed!')