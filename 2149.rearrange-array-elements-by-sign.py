#
# @lc app=leetcode id=2149 lang=python
#
# [2149] Rearrange Array Elements by Sign
#
# https://leetcode.com/problems/rearrange-array-elements-by-sign/description/
#
# algorithms
# Medium (82.22%)
# Likes:    2433
# Dislikes: 104
# Total Accepted:    162.2K
# Total Submissions: 197.3K
# Testcase Example:  '[3,1,-2,-5,2,-4]'
#
# You are given a 0-indexed integer array nums of even length consisting of an
# equal number of positive and negative integers.
#
# You should rearrange the elements of nums such that the modified array
# follows the given conditions:
#
#
# Every consecutive pair of integers have opposite signs.
# For all integers with the same sign, the order in which they were present in
# nums is preserved.
# The rearranged array begins with a positive integer.
#
#
# Return the modified array after rearranging the elements to satisfy the
# aforementioned conditions.
#
#
# Example 1:
#
#
# Input: nums = [3,1,-2,-5,2,-4]
# Output: [3,-2,1,-5,2,-4]
# Explanation:
# The positive integers in nums are [3,1,2]. The negative integers are
# [-2,-5,-4].
# The only possible way to rearrange them such that they satisfy all conditions
# is [3,-2,1,-5,2,-4].
# Other ways such as [1,-2,2,-5,3,-4], [3,1,2,-2,-5,-4], [-2,3,-5,1,-4,2] are
# incorrect because they do not satisfy one or more conditions.
#
#
# Example 2:
#
#
# Input: nums = [-1,1]
# Output: [1,-1]
# Explanation:
# 1 is the only positive integer and -1 the only negative integer in nums.
# So nums is rearranged to [1,-1].
#
#
#
# Constraints:
#
#
# 2 <= nums.length <= 2 * 10^5
# nums.length is even
# 1 <= |nums[i]| <= 10^5
# nums consists of equal number of positive and negative integers.
#
#
#

# @lc code=start
class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p = []
        n = []
        fn = [0]*len(nums)
        for i in range(len(nums)):
            if (nums[i] > 0):
                p.append(nums[i])
            elif (nums[i] < 0):
                n.append(nums[i])
        j = 0
        k = 0
        for i in range(len(fn)):
            if (i % 2 == 0):
                fn[i] = p[j]
                j += 1
            elif (i % 2 != 0):
                fn[i] = n[k]
                k += 1
        return fn

# @lc code=end
