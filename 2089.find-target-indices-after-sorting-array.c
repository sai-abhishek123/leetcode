/*
 * @lc app=leetcode id=2089 lang=c
 *
 * [2089] Find Target Indices After Sorting Array
 *
 * https://leetcode.com/problems/find-target-indices-after-sorting-array/description/
 *
 * algorithms
 * Easy (75.96%)
 * Likes:    1725
 * Dislikes: 81
 * Total Accepted:    158.2K
 * Total Submissions: 208.2K
 * Testcase Example:  '[1,2,5,2,3]\n2'
 *
 * You are given a 0-indexed integer array nums and a target element target.
 *
 * A target index is an index i such that nums[i] == target.
 *
 * Return a list of the target indices of nums after sorting nums in
 * non-decreasing order. If there are no target indices, return an empty list.
 * The returned list must be sorted in increasing order.
 *
 *
 * Example 1:
 *
 *
 * Input: nums = [1,2,5,2,3], target = 2
 * Output: [1,2]
 * Explanation: After sorting, nums is [1,2,2,3,5].
 * The indices where nums[i] == 2 are 1 and 2.
 *
 *
 * Example 2:
 *
 *
 * Input: nums = [1,2,5,2,3], target = 3
 * Output: [3]
 * Explanation: After sorting, nums is [1,2,2,3,5].
 * The index where nums[i] == 3 is 3.
 *
 *
 * Example 3:
 *
 *
 * Input: nums = [1,2,5,2,3], target = 5
 * Output: [4]
 * Explanation: After sorting, nums is [1,2,2,3,5].
 * The index where nums[i] == 5 is 4.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= nums.length <= 100
 * 1 <= nums[i], target <= 100
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
int *targetIndices(int *nums, int numsSize, int target, int *returnSize)
{
    int i, j, temp, count = 0;
    for (i = 0; i < numsSize; i++)
    {
        for (j = i + 1; j < numsSize; j++)
        {
            if (nums[i] > nums[j])
            {
                temp = nums[i];
                nums[i] = nums[j];
                nums[j] = temp;
            }
        }
    }
    for (i = 0; i < numsSize; i++)
    {
        if (nums[i] == target)
            count++;
    }
    *returnSize = count;
    int *arr = (int *)malloc(count * sizeof(int));
    j = 0;
    for (i = 0; i < numsSize; i++)
    {
        if (nums[i] == target)
        {
            arr[j] = i;
            j++;
        }
    }
    return arr;
}
// @lc code=end
