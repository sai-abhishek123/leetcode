#
# @lc app=leetcode id=372 lang=python
#
# [372] Super Pow
#
# https://leetcode.com/problems/super-pow/description/
#
# algorithms
# Medium (35.31%)
# Likes:    883
# Dislikes: 1415
# Total Accepted:    67.6K
# Total Submissions: 191.5K
# Testcase Example:  '2\n[3]'
#
# Your task is to calculate a^b mod 1337 where a is a positive integer and b is
# an extremely large positive integer given in the form of an array.
#
#
# Example 1:
#
#
# Input: a = 2, b = [3]
# Output: 8
#
#
# Example 2:
#
#
# Input: a = 2, b = [1,0]
# Output: 1024
#
#
# Example 3:
#
#
# Input: a = 1, b = [4,3,3,8,5,2]
# Output: 1
#
#
#
# Constraints:
#
#
# 1 <= a <= 2^31 - 1
# 1 <= b.length <= 2000
# 0 <= b[i] <= 9
# b does not contain leading zeros.
#
#
#

# @lc code=start
class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        MOD = 1337

        def modPow(x, y, mod):
            if y == 0:
                return 1
            half = modPow(x, y // 2, mod)
            if y % 2 == 0:
                return (half * half) % mod
            else:
                return (half * half * x) % mod
        result = 1
        for digit in b:
            result = modPow(result, 10, MOD) * modPow(a, digit, MOD) % MOD

        return result
# @lc code=end
