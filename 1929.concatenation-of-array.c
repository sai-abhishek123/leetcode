/*
 * @lc app=leetcode id=1929 lang=c
 *
 * [1929] Concatenation of Array
 *
 * https://leetcode.com/problems/concatenation-of-array/description/
 *
 * algorithms
 * Easy (89.61%)
 * Likes:    3101
 * Dislikes: 356
 * Total Accepted:    645.2K
 * Total Submissions: 720K
 * Testcase Example:  '[1,2,1]'
 *
 * Given an integer array nums of length n, you want to create an array ans of
 * length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n
 * (0-indexed).
 *
 * Specifically, ans is the concatenation of two nums arrays.
 *
 * Return the array ans.
 *
 *
 * Example 1:
 *
 *
 * Input: nums = [1,2,1]
 * Output: [1,2,1,1,2,1]
 * Explanation: The array ans is formed as follows:
 * - ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
 * - ans = [1,2,1,1,2,1]
 *
 * Example 2:
 *
 *
 * Input: nums = [1,3,2,1]
 * Output: [1,3,2,1,1,3,2,1]
 * Explanation: The array ans is formed as follows:
 * - ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
 * - ans = [1,3,2,1,1,3,2,1]
 *
 *
 *
 * Constraints:
 *
 *
 * n == nums.length
 * 1 <= n <= 1000
 * 1 <= nums[i] <= 1000
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
int *getConcatenation(int *nums, int numsSize, int *returnSize)
{
    *returnSize = numsSize * 2;
    // int size=numsSize*2,i;
    int i;
    int *a = (int *)malloc((numsSize * 2) * sizeof(int));
    for (i = 0; i < numsSize; i++)
    {
        a[i] = nums[i];
    }
    for (i = numsSize; i < (numsSize * 2); i++)
    {
        a[i] = nums[i - numsSize];
    }
    return a;
}
// @lc code=end
