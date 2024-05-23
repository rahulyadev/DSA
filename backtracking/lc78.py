""" LC78: Subsets(https://leetcode.com/problems/subsets/description/)."""
from typing import List

# Solution 1: Using backtracking(For loop)
# class Solution:
#     """Solution class for Subsets."""

#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         """Function to find all possible subsets."""
#         res = []
#         def backtrack(start, path):
#             print("start: ", start, "path: ", path)
#             res.append(path)
#             print("res: ", res)
#             for i in range(start, len(nums)):
#                 print("i: ", i)
#                 backtrack(i+1, path+[nums[i]])
#         backtrack(0, [])
#         return res

# Solution 2: Using backtracking(Recursion)
class Solution:
    """Solution class for Subsets."""
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """Function to find all possible subsets."""
        n = len(nums)
        res = []
        sol = []
        def backtrack(start):
            if start == n:
                res.append(sol[:])
                return
            
            backtrack(start + 1)
            sol.append(nums[start])
            backtrack(start+1)
            sol.pop()
        backtrack(0)
        return res
    
# Solution 3: Using Iterative approach
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         subsets = [[]]  # Start with the empty subset
        
#         for num in nums:
#             new_subsets = []
#             for subset in subsets:
#                 new_subset = subset + [num]  # Create a new subset by adding the current number
#                 new_subsets.append(new_subset)
#             subsets.extend(new_subsets)  # Add the new subsets to the list of all subsets
        
#         return subsets


# Solution 4: Using Bit Manipulation
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         n = len(nums)
#         all_subsets = []
        
#         # Iterate over all possible subsets (2^n)
#         for mask in range(1 << n):  # 1 << n generates the number of subsets (2^n)
#             subset = []
#             for i in range(n):
#                 # Check if the i-th bit is set in the mask
#                 if mask & (1 << i):  # 1 << i is used to check the i-th bit in mask
#                     subset.append(nums[i])
#             all_subsets.append(subset)
        
#         return all_subsets

test = Solution()
result = test.subsets([1,2,3])
if sorted(result) == sorted([[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]):
    print("Test case 1 is Passed")
else:
    print("Test case 1 is Failed")
result = test.subsets([0])
if result == [[],[0]]:
    print("Test case 2 is Passed")
else:
    print("Test case 2 is Failed")