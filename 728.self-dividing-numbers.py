#
# @lc app=leetcode id=728 lang=python
#
# [728] Self Dividing Numbers
#
# https://leetcode.com/problems/self-dividing-numbers/description/
#
# algorithms
# Easy (78.35%)
# Likes:    1728
# Dislikes: 368
# Total Accepted:    232.7K
# Total Submissions: 297K
# Testcase Example:  '1\n22'
#
# A self-dividing number is a number that is divisible by every digit it
# contains.
#
#
# For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 ==
# 0, and 128 % 8 == 0.
#
#
# A self-dividing number is not allowed to contain the digit zero.
#
# Given two integers left and right, return a list of all the self-dividing
# numbers in the range [left, right].
#
#
# Example 1:
# Input: left = 1, right = 22
# Output: [1,2,3,4,5,6,7,8,9,11,12,15,22]
# Example 2:
# Input: left = 47, right = 85
# Output: [48,55,66,77]
#
#
# Constraints:
#
#
# 1 <= left <= right <= 10^4
#
#
#

# @lc code=start
class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """

    def checker(self, n):
        t = n
        m = n
        count = 0
        while (n):
            rem = n % 10
            if rem == 0:
                break
            if (t % rem == 0):
                count += 1
            n /= 10
        if (count == len(str(m))):
            return True
        else:
            return False

    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        a = []
        for i in range(left, right+1):
            if self.checker(i) == True:
                a.append(i)
        return a

# @lc code=end
