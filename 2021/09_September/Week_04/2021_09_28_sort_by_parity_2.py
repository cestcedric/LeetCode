class Solution:
    # O(n) time: one pass to identify misplaced entries, one to swap
    # O(n) space: temporarily save indices of misplaced entries
    def sortArrayByParityIIstack(self, nums: list) -> list:
        wrongOdd = []
        wrongEven = []

        for i, n in enumerate(nums):
            if i % 2 != n % 2:
                if n % 2 == 0: wrongEven.append(i)
                else: wrongOdd.append(i)

        for odd, even in zip(wrongOdd, wrongEven):
            nums[odd], nums[even] = nums[even], nums[odd]

        return nums


    # O(n) time: one pass through array
    # O(1) space: only need space for two pointers
    def sortArrayByParityII(self, nums: list) -> list:
        IDXodd = 1

        for IDXeven in range(0, len(nums), 2):
            if nums[IDXeven] % 2 == 1:
                while nums[IDXodd] % 2 == 1:
                    IDXodd += 2

                nums[IDXodd], nums[IDXeven] = nums[IDXeven], nums[IDXodd]

        return nums


def validate(nums: list) -> bool:
    for i, n in enumerate(nums):
        if i % 2 != n % 2: return False
    return True


testcases = [
    ([4,2,5,7]),
    ([2,3]),
    ([1,2,3,4,5,6])
]

for i, (nums) in enumerate(testcases):
    output = Solution().sortArrayByParityII(nums)
    print('Case #{}: {}'.format(i + 1, output))
    assert validate(output)
print('All test cases passed!')