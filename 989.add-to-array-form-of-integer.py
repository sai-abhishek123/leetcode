#
# @lc app=leetcode id=989 lang=python
#
# [989] Add to Array-Form of Integer
#
# https://leetcode.com/problems/add-to-array-form-of-integer/description/
#
# algorithms
# Easy (45.71%)
# Likes:    3371
# Dislikes: 278
# Total Accepted:    250.5K
# Total Submissions: 548.7K
# Testcase Example:  '[1,2,0,0]\n34'
#
# The array-form of an integer num is an array representing its digits in left
# to right order.
#
#
# For example, for num = 1321, the array form is [1,3,2,1].
#
#
# Given num, the array-form of an integer, and an integer k, return the
# array-form of the integer num + k.
#
#
# Example 1:
#
#
# Input: num = [1,2,0,0], k = 34
# Output: [1,2,3,4]
# Explanation: 1200 + 34 = 1234
#
#
# Example 2:
#
#
# Input: num = [2,7,4], k = 181
# Output: [4,5,5]
# Explanation: 274 + 181 = 455
#
#
# Example 3:
#
#
# Input: num = [2,1,5], k = 806
# Output: [1,0,2,1]
# Explanation: 215 + 806 = 1021
#
#
#
# Constraints:
#
#
# 1 <= num.length <= 10^4
# 0 <= num[i] <= 9
# num does not contain any leading zeros except for the zero itself.
# 1 <= k <= 10^4
#
#
#

# @lc code=start
class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        string = ""
        final_array = []
        for i in range(len(num)):
            string += str(num[i])
        number = int(string)
        summing = str(number+k)
        summing = list(summing)
        for i in range(len(summing)):
            final_array.append(int(summing[i]))
        return final_array

# @lc code=end
