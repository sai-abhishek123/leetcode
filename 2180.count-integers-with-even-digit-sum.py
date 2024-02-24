#
# @lc app=leetcode id=2180 lang=python
#
# [2180] Count Integers With Even Digit Sum
#
# https://leetcode.com/problems/count-integers-with-even-digit-sum/description/
#
# algorithms
# Easy (66.44%)
# Likes:    592
# Dislikes: 27
# Total Accepted:    55K
# Total Submissions: 82.8K
# Testcase Example:  '4'
#
# Given a positive integer num, return the number of positive integers less
# than or equal to num whose digit sums are even.
#
# The digit sum of a positive integer is the sum of all its digits.
#
#
# Example 1:
#
#
# Input: num = 4
# Output: 2
# Explanation:
# The only integers less than or equal to 4 whose digit sums are even are 2 and
# 4.
#
#
# Example 2:
#
#
# Input: num = 30
# Output: 14
# Explanation:
# The 14 integers less than or equal to 30 whose digit sums are even are
# 2, 4, 6, 8, 11, 13, 15, 17, 19, 20, 22, 24, 26, and 28.
#
#
#
# Constraints:
#
#
# 1 <= num <= 1000
#
#
#

# @lc code=start
# class Solution(object):
class Solution(object):
    def counter(self, num):
        sum_i = 0
        while num:
            rem = num % 10
            sum_i += rem
            num //= 10
        return sum_i

    def countEven(self, num):
        """
        :type num: int
        :rtype: int
        """
        count = 0
        if self.counter(num) % 2 == 0:
            count += 1
        for i in range(1, num):
            if (self.counter(i) % 2 == 0):
                count += 1
        return count


# @lc code=end
