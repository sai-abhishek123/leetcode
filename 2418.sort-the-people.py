#
# @lc app=leetcode id=2418 lang=python
#
# [2418] Sort the People
#
# https://leetcode.com/problems/sort-the-people/description/
#
# algorithms
# Easy (79.97%)
# Likes:    1220
# Dislikes: 20
# Total Accepted:    118.5K
# Total Submissions: 148.2K
# Testcase Example:  '["Mary","John","Emma"]\n[180,165,170]'
#
# You are given an array of strings names, and an array heights that consists
# of distinct positive integers. Both arrays are of length n.
#
# For each index i, names[i] and heights[i] denote the name and height of the
# i^th person.
#
# Return names sorted in descending order by the people's heights.
#
#
# Example 1:
#
#
# Input: names = ["Mary","John","Emma"], heights = [180,165,170]
# Output: ["Mary","Emma","John"]
# Explanation: Mary is the tallest, followed by Emma and John.
#
#
# Example 2:
#
#
# Input: names = ["Alice","Bob","Bob"], heights = [155,185,150]
# Output: ["Bob","Alice","Bob"]
# Explanation: The first Bob is the tallest, followed by Alice and the second
# Bob.
#
#
#
# Constraints:
#
#
# n == names.length == heights.length
# 1 <= n <= 10^3
# 1 <= names[i].length <= 20
# 1 <= heights[i] <= 10^5
# names[i] consists of lower and upper case English letters.
# All the values of heights are distinct.
#
#
#

# @lc code=start
class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        for i in range(len(heights)):
            for j in range(i+1, len(heights), 1):
                if (heights[i] < heights[j]):
                    temp1 = heights[i]
                    temp2 = names[i]
                    heights[i] = heights[j]
                    names[i] = names[j]
                    heights[j] = temp1
                    names[j] = temp2
        print(names)
        print(heights)
        return names
# @lc code=end
