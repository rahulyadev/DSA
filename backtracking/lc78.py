""" LC78: Subsets(https://leetcode.com/problems/subsets/description/)."""
from typing import List

class Solution:
    """Solution class for Subsets."""

    def subsets(self, nums: List[int]) -> List[List[int]]:
        """Function to find all possible subsets."""
        res = []
        def backtrack(start, path):
            print("start: ", start, "path: ", path)
            res.append(path)
            print("res: ", res)
            for i in range(start, len(nums)):
                print("i: ", i)
                backtrack(i+1, path+[nums[i]])
        backtrack(0, [])
        return res


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
