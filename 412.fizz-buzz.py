#
# @lc app=leetcode id=412 lang=python
#
# [412] Fizz Buzz
#
# https://leetcode.com/problems/fizz-buzz/description/
#
# algorithms
# Easy (71.61%)
# Likes:    2587
# Dislikes: 347
# Total Accepted:    1.2M
# Total Submissions: 1.6M
# Testcase Example:  '3'
#
# Given an integer n, return a string array answer (1-indexed) where:
#
#
# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.
#
#
#
# Example 1:
# Input: n = 3
# Output: ["1","2","Fizz"]
# Example 2:
# Input: n = 5
# Output: ["1","2","Fizz","4","Buzz"]
# Example 3:
# Input: n = 15
# Output:
# ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
#
#
# Constraints:
#
#
# 1 <= n <= 10^4
#
#
#

# @lc code=start
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        a = [0]*n
        for i in range(1, n+1, 1):
            if (i % 3 == 0 and i % 5 == 0):
                a[i-1] = "FizzBuzz"
            elif (i % 3 == 0):
                a[i-1] = "Fizz"
            elif (i % 5 == 0):
                a[i-1] = "Buzz"
            else:
                a[i-1] = str(i)
        return a

# @lc code=end
