/*
 * @lc app=leetcode id=1051 lang=c
 *
 * [1051] Height Checker
 *
 * https://leetcode.com/problems/height-checker/description/
 *
 * algorithms
 * Easy (76.33%)
 * Likes:    1116
 * Dislikes: 79
 * Total Accepted:    322.8K
 * Total Submissions: 422.9K
 * Testcase Example:  '[1,1,4,2,1,3]'
 *
 * A school is trying to take an annual photo of all the students. The students
 * are asked to stand in a single file line in non-decreasing order by height.
 * Let this ordering be represented by the integer array expected where
 * expected[i] is the expected height of the i^th student in line.
 *
 * You are given an integer array heights representing the current order that
 * the students are standing in. Each heights[i] is the height of the i^th
 * student in line (0-indexed).
 *
 * Return the number of indices where heights[i] != expected[i].
 *
 *
 * Example 1:
 *
 *
 * Input: heights = [1,1,4,2,1,3]
 * Output: 3
 * Explanation:
 * heights:  [1,1,4,2,1,3]
 * expected: [1,1,1,2,3,4]
 * Indices 2, 4, and 5 do not match.
 *
 *
 * Example 2:
 *
 *
 * Input: heights = [5,1,2,3,4]
 * Output: 5
 * Explanation:
 * heights:  [5,1,2,3,4]
 * expected: [1,2,3,4,5]
 * All indices do not match.
 *
 *
 * Example 3:
 *
 *
 * Input: heights = [1,2,3,4,5]
 * Output: 0
 * Explanation:
 * heights:  [1,2,3,4,5]
 * expected: [1,2,3,4,5]
 * All indices match.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= heights.length <= 100
 * 1 <= heights[i] <= 100
 *
 *
 */

// @lc code=start
int heightChecker(int *heights, int heightsSize)
{
    int h[heightsSize], i, count = 0;
    for (i = 0; i < heightsSize; i++)
    {
        h[i] = heights[i];
    }
    for (i = 0; i < heightsSize; i++)
    {
        for (int j = i + 1; j < heightsSize; j++)
        {
            if (heights[i] > heights[j])
            {
                int temp = heights[i];
                heights[i] = heights[j];
                heights[j] = temp;
            }
        }
    }
    for (i = 0; i < heightsSize; i++)
    {
        if (heights[i] != h[i])
            count++;
    }
    return count;
}
// @lc code=end
