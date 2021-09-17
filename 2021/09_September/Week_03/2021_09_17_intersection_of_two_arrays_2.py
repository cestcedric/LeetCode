from collections import Counter

class Solution:
    # O(m + n) time: at most two passes through nums1, one through nums2
    # O(m + n) space: counters with at most as many entries as arrays
    def intersect(self, nums1: list, nums2: list) -> list:
        counter1, counter2 = Counter(nums1), Counter(nums2)
        output = []

        for key, value in counter1.items():
            output.extend([key] * min(value, counter2[key]))

        return output


    # O(m + n) time: assuming arrays are sorted, else obviously sorting time
    # O(1) space: only output allocated
    def intersectTwoPointers(self, nums1: list, nums2: list) -> list:
        nums1.sort()
        nums2.sort()

        p1, p2 = 0, 0

        output = []

        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] < nums2[p2]: p1 += 1
            elif nums1[p1] > nums2[p2]: p2 += 1
            else:
                output.append(nums1[p1])
                p1 +=1 
                p2 +=1

        return output
            


testcases = [
    ([1,2,2,1], [2,2], [2,2]),
    ([4,9,5], [9,4,9,8,4], [4,9])
]

for i, (nums1, nums2, target) in enumerate(testcases):
    output = Solution().intersect(nums1, nums2)
    print('Case #{}: should be\n{}, is\n{}'.format(i + 1, sorted(target), sorted(output)))
    assert target == output
print('All test cases passed!')