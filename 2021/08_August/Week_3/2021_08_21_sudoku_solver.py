class Solution:
    # O(n ^ (n^2)) time: probably, for n x n board
    # => each backtrack step in O(1)
    # at most n tries, for a little under n^2 fields on the board
    # O(n) space: row, col and box dictionaries for 1..n
    def solveSudoku(self, board: list) -> None:

        BOARDSIZE = 9
        GRIDSIZE = 3

        checkRow = [set() for _ in range(BOARDSIZE)]
        checkCol = [set() for _ in range(BOARDSIZE)]
        checkBox = [set() for _ in range(BOARDSIZE)]

        toFill = []
        for x in range(BOARDSIZE):
            for y in range(BOARDSIZE):
                if board[x][y] == '.':
                    toFill.append((x, y))
                else:
                    checkRow[int(board[x][y]) - 1].add(x)
                    checkCol[int(board[x][y]) - 1].add(y)
                    checkBox[int(board[x][y]) - 1].add((x // GRIDSIZE, y // GRIDSIZE))

        def backtrack(i):
            nonlocal toFill
            nonlocal BOARDSIZE, GRIDSIZE
            nonlocal board, checkRow, checkCol, checkBox

            if i == len(toFill): return True

            x, y = toFill[i]

            for n in range(BOARDSIZE):
                # n here already not possible
                if x in checkRow[n] \
                or y in checkCol[n] \
                or (x // GRIDSIZE, y // GRIDSIZE) in checkBox[n]:
                    continue

                # try it out and hope for the best
                board[x][y] = str(n + 1)
                checkRow[n].add(x)
                checkCol[n].add(y)
                checkBox[n].add((x // GRIDSIZE, y // GRIDSIZE))

                if backtrack(i + 1): 
                    return True
                
                # did not work, try next
                checkRow[n].remove(x)
                checkCol[n].remove(y)
                checkBox[n].remove((x // GRIDSIZE, y // GRIDSIZE))

            # unsolvable situation, go back
            return False

        backtrack(0)


testcases = [
    ([['5','3','.','.','7','.','.','.','.']
     ,['6','.','.','1','9','5','.','.','.']
     ,['.','9','8','.','.','.','.','6','.']
     ,['8','.','.','.','6','.','.','.','3']
     ,['4','.','.','8','.','3','.','.','1']
     ,['7','.','.','.','2','.','.','.','6']
     ,['.','6','.','.','.','.','2','8','.']
     ,['.','.','.','4','1','9','.','.','5']
     ,['.','.','.','.','8','.','.','7','9']],
     [['5','3','4','6','7','8','9','1','2']
     ,['6','7','2','1','9','5','3','4','8']
     ,['1','9','8','3','4','2','5','6','7']
     ,['8','5','9','7','6','1','4','2','3']
     ,['4','2','6','8','5','3','7','9','1']
     ,['7','1','3','9','2','4','8','5','6']
     ,['9','6','1','5','3','7','2','8','4']
     ,['2','8','7','4','1','9','6','3','5']
     ,['3','4','5','2','8','6','1','7','9']])
]

for i, (board, target) in enumerate(testcases):
    Solution().solveSudoku(board)
    print('Case #{}: should be'.format(i + 1))
    for row in target:
        print(row)
    print('result:')
    for row in board:
        print(row)
    assert target == board
print('All test cases passed!')

            



                        
