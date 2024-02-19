#
# @lc app=leetcode id=693 lang=python
#
# [693] Binary Number with Alternating Bits
#
# https://leetcode.com/problems/binary-number-with-alternating-bits/description/
#
# algorithms
# Easy (62.12%)
# Likes:    1330
# Dislikes: 110
# Total Accepted:    128.7K
# Total Submissions: 206.9K
# Testcase Example:  '5'
#
# Given a positive integer, check whether it has alternating bits: namely, if
# two adjacent bits will always have different values.
#
#
# Example 1:
#
#
# Input: n = 5
# Output: true
# Explanation: The binary representation of 5 is: 101
#
#
# Example 2:
#
#
# Input: n = 7
# Output: false
# Explanation: The binary representation of 7 is: 111.
#
# Example 3:
#
#
# Input: n = 11
# Output: false
# Explanation: The binary representation of 11 is: 1011.
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
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        binary = bin(n).replace("0b", "")
        binary_list = list(binary)
        for i in range(1, len(binary_list)):
            result = int(binary_list[i-1]) ^ int(binary_list[i])
            if result == 0:
                return False
        return True

# @lc code=end
