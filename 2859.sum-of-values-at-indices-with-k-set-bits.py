#
# @lc app=leetcode id=2859 lang=python
#
# [2859] Sum of Values at Indices With K Set Bits
#
# https://leetcode.com/problems/sum-of-values-at-indices-with-k-set-bits/description/
#
# algorithms
# Easy (86.25%)
# Likes:    206
# Dislikes: 27
# Total Accepted:    50.6K
# Total Submissions: 58.6K
# Testcase Example:  '[5,10,1,5,2]\n1'
#
# You are given a 0-indexed integer array nums and an integer k.
#
# Return an integer that denotes the sum of elements in nums whose
# corresponding indices have exactly k set bits in their binary
# representation.
#
# The set bits in an integer are the 1's present when it is written in
# binary.
#
#
# For example, the binary representation of 21 is 10101, which has 3 set
# bits.
#
#
#
# Example 1:
#
#
# Input: nums = [5,10,1,5,2], k = 1
# Output: 13
# Explanation: The binary representation of the indices are:
# 0 = 0002
# 1 = 0012
# 2 = 0102
# 3 = 0112
# 4 = 1002
# Indices 1, 2, and 4 have k = 1 set bits in their binary representation.
# Hence, the answer is nums[1] + nums[2] + nums[4] = 13.
#
# Example 2:
#
#
# Input: nums = [4,3,2,1], k = 2
# Output: 1
# Explanation: The binary representation of the indices are:
# 0 = 002
# 1 = 012
# 2 = 102
# 3 = 112
# Only index 3 has k = 2 set bits in its binary representation.
# Hence, the answer is nums[3] = 1.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 10^5
# 0 <= k <= 10
#
#
#

# @lc code=start
class Solution(object):
    def sumIndicesWithKSetBits(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

    def decimal_to_binary(self, n):
        return bin(n).replace('0b', "")

    def binary_to_decimal(self, n):
        return int(n, 2)

    def count_ones(self, i):
        c = 0
        while (i):
            rem = i % 10
            if rem == 1:
                c += 1
            i = i//10
        return c

    def sumIndicesWithKSetBits(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        array2 = []
        array = []
        for i in range(len(nums)):
            checker = self.decimal_to_binary(i)
            array.append(checker)
        for i in range(len(array)):
            if self.count_ones(int(array[i])) == k:
                array2.append(array[i])
        for i in range(len(array2)):
            array2[i] = self.binary_to_decimal(array2[i])
        a3 = []
        for i in range(len(array2)):
            a3.append(nums[array2[i]])
        sum1 = 0
        for i in range(len(a3)):
            sum1 = sum1+a3[i]
        return sum1

# @lc code=end
