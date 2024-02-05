#
# @lc app=leetcode id=400 lang=python
#
# [400] Nth Digit
#
# https://leetcode.com/problems/nth-digit/description/
#
# algorithms
# Medium (34.57%)
# Likes:    1032
# Dislikes: 2005
# Total Accepted:    93.1K
# Total Submissions: 269.2K
# Testcase Example:  '3'
#
# Given an integer n, return the n^th digit of the infinite integer sequence
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...].
#
#
# Example 1:
#
#
# Input: n = 3
# Output: 3
#
#
# Example 2:
#
#
# Input: n = 11
# Output: 0
# Explanation: The 11^th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
# 11, ... is a 0, which is part of the number 10.
#
#
#
# Constraints:
#
#
# 1 <= n <= 2^31 - 1
#
#
#

# @lc code=start
class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0

        digit_size = 1
        while True:
            count = 9 * 10 ** (digit_size - 1) * digit_size
            if n <= count:
                break
            n -= count
            digit_size += 1

        num = 10 ** (digit_size - 1) + (n - 1) // digit_size
        position = (n - 1) % digit_size

        return int(str(num)[position])
# @lc code=end
