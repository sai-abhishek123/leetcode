#
# @lc app=leetcode id=771 lang=python
#
# [771] Jewels and Stones
#
# https://leetcode.com/problems/jewels-and-stones/description/
#
# algorithms
# Easy (88.42%)
# Likes:    5004
# Dislikes: 583
# Total Accepted:    1M
# Total Submissions: 1.1M
# Testcase Example:  '"aA"\n"aAAbbbb"'
#
# You're given strings jewels representing the types of stones that are jewels,
# and stones representing the stones you have. Each character in stones is a
# type of stone you have. You want to know how many of the stones you have are
# also jewels.
#
# Letters are case sensitive, so "a" is considered a different type of stone
# from "A".
#
#
# Example 1:
# Input: jewels = "aA", stones = "aAAbbbb"
# Output: 3
# Example 2:
# Input: jewels = "z", stones = "ZZ"
# Output: 0
#
#
# Constraints:
#
#
# 1 <= jewels.length, stones.length <= 50
# jewels and stones consist of only English letters.
# All the characters of jewels are unique.
#
#
#

# @lc code=start
class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        list_jewels = list(jewels)
        list_stones = list(stones)
        return len(list(filter(lambda x: x in list_jewels, list_stones)))

# @lc code=end
