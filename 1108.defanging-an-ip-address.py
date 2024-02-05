#
# @lc app=leetcode id=1108 lang=python
#
# [1108] Defanging an IP Address
#
# https://leetcode.com/problems/defanging-an-ip-address/description/
#
# algorithms
# Easy (88.91%)
# Likes:    2018
# Dislikes: 1743
# Total Accepted:    610.6K
# Total Submissions: 686.8K
# Testcase Example:  '"1.1.1.1"'
#
# Given a valid (IPv4) IP address, return a defanged version of that IP
# address.
#
# A defanged IP address replaces every period "." with "[.]".
#
#
# Example 1:
# Input: address = "1.1.1.1"
# Output: "1[.]1[.]1[.]1"
# Example 2:
# Input: address = "255.100.50.0"
# Output: "255[.]100[.]50[.]0"
#
#
# Constraints:
#
#
# The given address is a valid IPv4 address.
#
#

# @lc code=start
class Solution(object):
    def defangIPaddr(self, address):
        return (address.replace(".", "[.]"))

# @lc code=end
