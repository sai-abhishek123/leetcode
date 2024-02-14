#
# @lc app=leetcode id=657 lang=python
#
# [657] Robot Return to Origin
#
# https://leetcode.com/problems/robot-return-to-origin/description/
#
# algorithms
# Easy (75.62%)
# Likes:    2363
# Dislikes: 740
# Total Accepted:    412.7K
# Total Submissions: 545.7K
# Testcase Example:  '"UD"'
#
# There is a robot starting at the position (0, 0), the origin, on a 2D plane.
# Given a sequence of its moves, judge if this robot ends up at (0, 0) after it
# completes its moves.
#
# You are given a string moves that represents the move sequence of the robot
# where moves[i] represents its i^th move. Valid moves are 'R' (right), 'L'
# (left), 'U' (up), and 'D' (down).
#
# Return true if the robot returns to the origin after it finishes all of its
# moves, or false otherwise.
#
# Note: The way that the robot is "facing" is irrelevant. 'R' will always make
# the robot move to the right once, 'L' will always make it move left, etc.
# Also, assume that the magnitude of the robot's movement is the same for each
# move.
#
#
# Example 1:
#
#
# Input: moves = "UD"
# Output: true
# Explanation: The robot moves up once, and then down once. All moves have the
# same magnitude, so it ended up at the origin where it started. Therefore, we
# return true.
#
#
# Example 2:
#
#
# Input: moves = "LL"
# Output: false
# Explanation: The robot moves left twice. It ends up two "moves" to the left
# of the origin. We return false because it is not at the origin at the end of
# its moves.
#
#
#
# Constraints:
#
#
# 1 <= moves.length <= 2 * 10^4
# moves only contains the characters 'U', 'D', 'L' and 'R'.
#
#
#

# @lc code=start
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        list_moves = list(moves)
        final_answer_x = 0
        final_answer_y = 0
        for i in range(len(list_moves)):
            if list_moves[i] == 'U':
                final_answer_x += 1
            elif list_moves[i] == 'D':
                final_answer_x -= 1
            elif list_moves[i] == 'L':
                final_answer_y += 1
            elif list_moves[i] == 'R':
                final_answer_y -= 1
        if final_answer_y or final_answer_x:
            return False
        return True

# @lc code=end
