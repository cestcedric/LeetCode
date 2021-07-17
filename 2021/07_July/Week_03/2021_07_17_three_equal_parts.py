class Solution:
    # O(n) time complexity: one pass through arr
    # One additional pass through ones, with <= n elements
    # O(n) space complexity: ones with at most n entries
    def threeEqualParts(self, arr: list) -> list:
        ones = [i for i, a in enumerate(arr) if a == 1]
        n, o = len(arr), len(ones)
        # can't evenly distribute 1s
        if o % 3 != 0: return [-1, -1]
        if o == 0: return [0, n - 1]

        # last part is the one with the fixed length,
        # do the others have space to accomodate that
        i_1, i_2, i_3 = 0, o // 3, o // 3 * 2
        len_1 = ones[i_2] - ones[i_1]
        len_2 = ones[i_3] - ones[i_2]
        len_3 = n - ones[i_3]
        if len_3 > len_1 or len_3 > len_2: return [-1, -1]

        # are there enough 0s at the end of part 1 and 2 to match 3
        zeros_1 = ones[i_2] - ones[i_2 - 1]
        zeros_2 = ones[i_3] - ones[i_3 - 1]
        zeros_3 = n - ones[o - 1]
        if zeros_3 > zeros_1 or zeros_3 > zeros_2: return [-1, -1]

        # actually compare pattern
        for i in range(o // 3 - 1):
            d_1 = ones[i_1 + i + 1] - ones[i_1 + i]
            d_2 = ones[i_2 + i + 1] - ones[i_2 + i]
            d_3 = ones[i_3 + i + 1] - ones[i_3 + i]
            if not d_1 == d_2 == d_3: return [-1, -1]

        zeroOffsetAtEnd = n - ones[-1] - 1
        return [ones[i_2 - 1] + zeroOffsetAtEnd, ones[i_3 - 1] + zeroOffsetAtEnd + 1]
        



        # positions of 1s
        # relative distance has to be equal
        # number of zeros behind last 1 of each part has to be 
        # equal to number of zeros between last 1 overall and end


testcases = [
    ([1,0,1,0,1], [0, 3]),
    ([1,1,0,1,1], [-1, -1]),
    ([1,1,0,0,1], [0, 2])
]

for i, (arr, target) in enumerate(testcases):
    output = Solution().threeEqualParts(arr)
    print('Case #{}: should be {}, is {}'.format(i + 1, target, output))
    assert target == output
print('All test cases passed')
        