/*
 * @lc app=leetcode id=1480 lang=c
 *
 * [1480] Running Sum of 1d Array
 *
 * https://leetcode.com/problems/running-sum-of-1d-array/description/
 *
 * algorithms
 * Easy (86.64%)
 * Likes:    7619
 * Dislikes: 340
 * Total Accepted:    1.7M
 * Total Submissions: 2M
 * Testcase Example:  '[1,2,3,4]'
 *
 * Given an array nums. We define a running sum of an array as runningSum[i] =
 * sum(nums[0]…nums[i]).
 *
 * Return the running sum of nums.
 *
 *
 * Example 1:
 *
 *
 * Input: nums = [1,2,3,4]
 * Output: [1,3,6,10]
 * Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
 *
 * Example 2:
 *
 *
 * Input: nums = [1,1,1,1,1]
 * Output: [1,2,3,4,5]
 * Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1,
 * 1+1+1+1+1].
 *
 * Example 3:
 *
 *
 * Input: nums = [3,1,2,10,1]
 * Output: [3,4,6,16,17]
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= nums.length <= 1000
 * -10^6 <= nums[i] <= 10^6
 *
 */

// @lc code=start
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int *runningSum(int *nums, int numsSize, int *returnSize)
{
    for (int i = 1; i < numsSize; i++)
    {
        nums[i] += nums[i - 1];
    }
    *returnSize = numsSize;
    return nums;
}
// @lc code=end
