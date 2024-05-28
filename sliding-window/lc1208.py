"""LC1208: Get Equal Substrings Within Budget.
(https://leetcode.com/problems/get-equal-substrings-within-budget/)
"""

class Solution:
    """Solution class for Get Equal Substrings Within Budget."""
    def equal_substring(self, s: str, t: str, max_cost: int) -> int:
        """Function to find the maximum length of a substring of s
        that can be changed to be the same as t.
        """
        left = 0
        current_cost = 0
        max_length = 0

        for right, _ in enumerate(s):
            current_cost += abs(ord(s[right]) - ord(t[right]))

            while current_cost > max_cost:
                current_cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length
