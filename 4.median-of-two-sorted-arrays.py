#
# @lc app=leetcode id=4 lang=python
#
# [4] Median of Two Sorted Arrays
#
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (39.16%)
# Likes:    27411
# Dislikes: 3020
# Total Accepted:    2.4M
# Total Submissions: 6.1M
# Testcase Example:  '[1,3]\n[2]'
#
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return
# the median of the two sorted arrays.
#
# The overall run time complexity should be O(log (m+n)).
#
#
# Example 1:
#
#
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
#
#
# Example 2:
#
#
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
#
#
#
# Constraints:
#
#
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -10^6 <= nums1[i], nums2[i] <= 10^6
#
#
#

# @lc code=start
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        sum1 = len(nums1)+len(nums2)
        a = [0]*sum1
        for i in range(len(nums1)):
            a[i] = nums1[i]
        for i in range(len(nums1), sum1, 1):
            a[i] = nums2[sum1-i-1]
        a.sort()
        if (sum1 % 2 != 0):
            return (a[sum1/2])
        elif (sum1 % 2 == 0):
            val1 = a[sum1/2-1]
            val2 = a[sum1/2]
            med = float(val1+val2)/2
            return med

# @lc code=end
