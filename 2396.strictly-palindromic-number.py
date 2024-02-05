#
# @lc app=leetcode id=2396 lang=python
#
# [2396] Strictly Palindromic Number
#
# https://leetcode.com/problems/strictly-palindromic-number/description/
#
# algorithms
# Medium (87.32%)
# Likes:    552
# Dislikes: 1470
# Total Accepted:    74.9K
# Total Submissions: 85.8K
# Testcase Example:  '9'
#
# An integer n is strictly palindromic if, for every base b between 2 and n - 2
# (inclusive), the string representation of the integer n in base b is
# palindromic.
#
# Given an integer n, return true if n is strictly palindromic and false
# otherwise.
#
# A string is palindromic if it reads the same forward and backward.
#
#
# Example 1:
#
#
# Input: n = 9
# Output: false
# Explanation: In base 2: 9 = 1001 (base 2), which is palindromic.
# In base 3: 9 = 100 (base 3), which is not palindromic.
# Therefore, 9 is not strictly palindromic so we return false.
# Note that in bases 4, 5, 6, and 7, n = 9 is also not palindromic.
#
#
# Example 2:
#
#
# Input: n = 4
# Output: false
# Explanation: We only consider base 2: 4 = 100 (base 2), which is not
# palindromic.
# Therefore, we return false.
#
#
#
#
# Constraints:
#
#
# 4 <= n <= 10^5
#
#
#

# @lc code=start
class Solution(object):
    def isStrictlyPalindromic(self, n):
        temp1 = n
        for k in range(2, temp1-1):
            sum_val = 0
            count = 0
            temp = temp1
            n = temp1
            while n:
                count += 1
                n //= k
            arr = []
            while temp:
                rem = temp % k
                arr.append(rem)
                temp //= k
            for val in reversed(arr):
                sum_val = sum_val * 10 + val
            sum1 = sum_val
            sum2 = 0
            while (sum_val):
                rem = sum_val % 10
                sum2 = sum2*10+rem
                sum_val //= 10
            if (sum2 != sum1):
                return False
                break
        return True
# @lc code=end
