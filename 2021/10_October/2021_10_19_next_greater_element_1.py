class Solution:
    # O(m + n) time: m = len(nums1), n = len(nums2)
    # O(n) space
    def nextGreaterElement(self, nums1: list, nums2: list) -> list:
        
        nextGreater = {n: -1 for n in nums2}
        stack = []
        
        for i, n in enumerate(nums2):
            
            while not stack == []:
                if n < stack[-1]: break
                nextGreater[stack[-1]] = n
                stack.pop()
            stack.append(n)
            
        return [nextGreater[n] for n in nums1]