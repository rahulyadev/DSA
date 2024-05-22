# LC131: (https://leetcode.com/problems/palindrome-partitioning/description/)

from typing import List


class Solution:
    """Solution class for Palindrome Partitioning."""
    def partition(self, s: str) -> List[List[str]]:
        """Function to find all possible palindrome partitioning."""
        res = []
        sol = []
        def backtrack(start):
            if start == len(s):
                res.append(sol[:])
                return
            for end in range(start, len(s)):
                if s[start:end+1] == s[start:end+1][::-1]:
                    sol.append(s[start:end+1])
                    backtrack(end+1)
                    sol.pop()
        backtrack(0)
        return res