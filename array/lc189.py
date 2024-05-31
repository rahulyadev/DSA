"""LC189: Rotate Array.
(https://leetcode.com/problems/rotate-array/).
"""

from typing import List

# Best solution
class Solution:
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        self.reverse(nums, 0, n-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, n-1)

# Approach 2: Using O(k) space
# Time complexity: O(n)
# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         n = len(nums)
#         k = k % n
#         d = []
#         for i in range(k):
#             d.append(nums[n-k+i])
#         for j in range(n-k-1, -1, -1):
#             nums[j+k] = nums[j]
#         for i in range(k):
#             nums[i] = d[i]

# Approach 3: Brute Force
# Time complexity: O(n*k)
# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         n = len(nums)
#         k = k % n
#         for i in range(k):
#             previous = nums[-1]
#             for j in range(n):
#                 nums[j], previous = previous, nums[j]
