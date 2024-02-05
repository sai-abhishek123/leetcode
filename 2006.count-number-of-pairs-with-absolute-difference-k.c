/*
 * @lc app=leetcode id=2006 lang=c
 *
 * [2006] Count Number of Pairs With Absolute Difference K
 *
 * https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/description/
 *
 * algorithms
 * Easy (83.40%)
 * Likes:    1567
 * Dislikes: 40
 * Total Accepted:    132.5K
 * Total Submissions: 158.9K
 * Testcase Example:  '[1,2,2,1]\n1'
 *
 * Given an integer array nums and an integer k, return the number of pairs (i,
 * j) where i < j such that |nums[i] - nums[j]| == k.
 *
 * The value of |x| is defined as:
 *
 *
 * x if x >= 0.
 * -x if x < 0.
 *
 *
 *
 * Example 1:
 *
 *
 * Input: nums = [1,2,2,1], k = 1
 * Output: 4
 * Explanation: The pairs with an absolute difference of 1 are:
 * - [1,2,2,1]
 * - [1,2,2,1]
 * - [1,2,2,1]
 * - [1,2,2,1]
 *
 *
 * Example 2:
 *
 *
 * Input: nums = [1,3], k = 3
 * Output: 0
 * Explanation: There are no pairs with an absolute difference of 3.
 *
 *
 * Example 3:
 *
 *
 * Input: nums = [3,2,1,5,4], k = 2
 * Output: 3
 * Explanation: The pairs with an absolute difference of 2 are:
 * - [3,2,1,5,4]
 * - [3,2,1,5,4]
 * - [3,2,1,5,4]
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= nums.length <= 200
 * 1 <= nums[i] <= 100
 * 1 <= k <= 99
 *
 *
 */

// @lc code=start
#include <math.h>
#include <stdlib.h>
int countKDifference(int *nums, int numsSize, int k)
{
    int i, j, count = 0;
    for (i = 0; i < numsSize; i++)
    {
        for (j = i + 1; j < numsSize; j++)
        {
            if (abs(nums[i] - nums[j]) == k && i < j)
            {
                count++;
            }
        }
    }
    return count;
}
// @lc code=end
