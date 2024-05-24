"""LC1177: Can Make Palindrome from Substring
(https://leetcode.com/problems/can-make-palindrome-from-substring/description/)
"""

from typing import List

class Solution:
    """Solution class for Can Make Palindrome from Substring."""
    def can_make_pali_queries(self, s: str, queries: List[List[int]]) -> List[bool]:
        """Function to check if it is possible to make a palindrome from the substring."""
        # Step 1: Create a prefix sum of character counts
        n = len(s)
        prefix = [[0] * 26 for _ in range(n + 1)]

        for i in range(n):
            prefix[i + 1] = prefix[i][:]
            prefix[i + 1][ord(s[i]) - ord('a')] += 1

        # Step 2: Process each query
        res = []
        for left, right, k in queries:
            odd_count = 0
            for j in range(26):
                if (prefix[right + 1][j] - prefix[left][j]) % 2 == 1:
                    odd_count += 1
            # To make a palindrome, we need at most (odd_count // 2) replacements
            res.append(odd_count // 2 <= k)

        return res
