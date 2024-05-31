"""LC260: Single Number III
(https://leetcode.com/problems/single-number-iii/).
"""

from typing import List

class Solution:
    """Bit Manipulation"""

    def single_number(self, nums: List[int]) -> List[int]:
        """Main function to find the two unique numbers in the list."""
        # Step 1: XOR all numbers to get XOR of the two unique numbers
        xor_result = 0
        for num in nums:
            xor_result ^= num

        # Step 2: Find any bit that is set in xor_result
        diff_bit = xor_result & -xor_result

        # Step 3: Partition the numbers into two groups and XOR within each group
        a, b = 0, 0
        for num in nums:
            if num & diff_bit:
                a ^= num
            else:
                b ^= num

        return [a, b]
        