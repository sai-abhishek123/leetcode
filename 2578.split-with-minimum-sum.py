#
# @lc app=leetcode id=2578 lang=python
#
# [2578] Split With Minimum Sum
#
# https://leetcode.com/problems/split-with-minimum-sum/description/
#
# algorithms
# Easy (69.65%)
# Likes:    337
# Dislikes: 28
# Total Accepted:    30.6K
# Total Submissions: 43.9K
# Testcase Example:  '4325'
#
# Given a positive integer num, split it into two non-negative integers num1
# and num2 such that:
#
#
# The concatenation of num1 and num2 is a permutation of num.
#
#
# In other words, the sum of the number of occurrences of each digit in num1
# and num2 is equal to the number of occurrences of that digit in
# num.
#
#
# num1 and num2 can contain leading zeros.
#
#
# Return the minimum possible sum of num1 and num2.
#
# Notes:
#
#
# It is guaranteed that num does not contain any leading zeros.
# The order of occurrence of the digits in num1 and num2 may differ from the
# order of occurrence of num.
#
#
#
# Example 1:
#
#
# Input: num = 4325
# Output: 59
# Explanation: We can split 4325 so that num1 is 24 and num2 is 35, giving a
# sum of 59. We can prove that 59 is indeed the minimal possible sum.
#
#
# Example 2:
#
#
# Input: num = 687
# Output: 75
# Explanation: We can split 687 so that num1 is 68 and num2 is 7, which would
# give an optimal sum of 75.
#
#
#
# Constraints:
#
#
# 10 <= num <= 10^9
#
#
#

# @lc code=start
class Solution(object):
    def splitNum(self, num):
        """
        :type num: int
        :rtype: int
        """
        final_array = []
        odd_positions = []
        even_positions = []
        sum_odd = 0
        sum_even = 0
        while (num):
            rem = num % 10
            final_array.append(rem)
            num = num//10
        final_array.sort()
        for i in range(len(final_array)):
            if (i % 2 == 0):
                odd_positions.append(final_array[i])
            else:
                even_positions.append(final_array[i])
        for i in range(len(odd_positions)):
            sum_odd = sum_odd*10+odd_positions[i]
        for i in range(len(even_positions)):
            sum_even = sum_even*10+even_positions[i]
        return (sum_odd+sum_even)

# @lc code=end
