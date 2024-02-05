/*
 * @lc app=leetcode id=2574 lang=c
 *
 * [2574] Left and Right Sum Differences
 *
 * https://leetcode.com/problems/left-and-right-sum-differences/description/
 *
 * algorithms
 * Easy (86.00%)
 * Likes:    949
 * Dislikes: 76
 * Total Accepted:    108.1K
 * Total Submissions: 125.7K
 * Testcase Example:  '[10,4,8,3]'
 *
 * Given a 0-indexed integer array nums, find a 0-indexed integer array answer
 * where:
 *
 *
 * ⁠   answer.length == nums.length.
 * ⁠   answer[i] = |leftSum[i] - rightSum[i]|.
 *
 *
 * Where:
 *
 *
 * ⁠   leftSum[i] is the sum of elements to the left of the index i in the
 * array nums. If there is no such element, leftSum[i] = 0.
 * ⁠   rightSum[i] is the sum of elements to the right of the index i in the
 * array nums. If there is no such element, rightSum[i] = 0.
 *
 *
 * Return the array answer.
 *
 *
 * Example 1:
 *
 *
 * Input: nums = [10,4,8,3]
 * Output: [15,1,11,22]
 * Explanation: The array leftSum is [0,10,14,22] and the array rightSum is
 * [15,11,3,0].
 * The array answer is [|0 - 15|,|10 - 11|,|14 - 3|,|22 - 0|] = [15,1,11,22].
 *
 *
 * Example 2:
 *
 *
 * Input: nums = [1]
 * Output: [0]
 * Explanation: The array leftSum is [0] and the array rightSum is [0].
 * The array answer is [|0 - 0|] = [0].
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= nums.length <= 1000
 * 1 <= nums[i] <= 10^5
 *
 *
 */

// @lc code=start
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
#include <math.h>
int *leftRightDifference(int *nums, int numsSize, int *returnSize)
{
    int *la = (int *)malloc(numsSize * sizeof(int));
    int *ra = (int *)malloc(numsSize * sizeof(int));
    int i, j;
    la[0] = 0;
    ra[numsSize - 1] = 0;
    for (i = 1; i < numsSize; i++)
    {
        la[i] = la[i - 1] + nums[i - 1];
    }
    for (i = numsSize - 2; i >= 0; i--)
    {
        ra[i] = ra[i + 1] + nums[i + 1];
    }
    int *result = (int *)malloc(numsSize * sizeof(int));
    for (i = 0; i < numsSize; i++)
    {
        result[i] = abs(la[i] - ra[i]);
    }
    *returnSize = numsSize;
    return result;
}
// @lc code=end
