#
# @lc app=leetcode id=349 lang=python
#
# [349] Intersection of Two Arrays
#
# https://leetcode.com/problems/intersection-of-two-arrays/description/
#
# algorithms
# Easy (72.22%)
# Likes:    5498
# Dislikes: 2233
# Total Accepted:    995.1K
# Total Submissions: 1.4M
# Testcase Example:  '[1,2,2,1]\n[2,2]'
#
# Given two integer arrays nums1 and nums2, return an array of their
# intersection. Each element in the result must be unique and you may return
# the result in any order.
#
#
# Example 1:
#
#
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
#
#
# Example 2:
#
#
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.
#
#
#
# Constraints:
#
#
# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000
#
#
#

# @lc code=start
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        b = []
        if (len(nums1) > len(nums2)):
            for i in range(len(nums2)):
                if nums2[i] in nums1:
                    b.append(nums2[i])
        elif (len(nums1) <= len(nums2)):
            for i in range(len(nums1)):
                if nums1[i] in nums2:
                    b.append(nums1[i])
        c = []*len(b)
        for i in b:
            if i not in c:
                c.append(i)
        return c
# @lc code=end
