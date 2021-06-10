class NumMatrix:

    def __init__(self, matrix: list):
        # save original data (not needed really)
        # self.matrix = matrix
        # precompute sums for all regions (0,0) -> (row, column)
        self.regions = []
        self.regions.append([matrix[0][0]])
        for column in range(1, len(matrix[0])):
            self.regions[0].append(matrix[0][column] + self.regions[0][column-1])

        for row in range(1, len(matrix)):
            newRow = [matrix[row][0] + self.regions[-1][0]]
            for column in range(1, len(matrix[0])):
                totalArea = matrix[row][column]
                totalArea += newRow[column-1]
                totalArea += self.regions[row-1][column]
                totalArea -= self.regions[row-1][column-1]
                newRow.append(totalArea)
            self.regions.append(newRow)


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # compute are from (a,b) -> (c,d) based on the precomputed areas starting from (0,0)
        # use inclusion/exclusion
        total = self.regions[row2][col2]
        total -= self.regions[row1-1][col2] if row1 > 0 else 0
        total -= self.regions[row2][col1-1] if col1 > 0 else 0
        total += self.regions[row1-1][col1-1] if row1 > 0 and col1 > 0 else 0
        return total
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
m = NumMatrix(matrix)
print('Should be 8: {}'.format(m.sumRegion(2, 1, 4, 3)))
print('Should be 11: {}'.format(m.sumRegion(1, 1, 2, 2)))
print('Should be 12: {}'.format(m.sumRegion(1, 2, 2, 4)))
print('Should be 3: {}'.format(m.sumRegion(0, 0, 0, 0)))