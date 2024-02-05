/*
 * @lc app=leetcode id=1470 lang=c
 *
 * [1470] Shuffle the Array
 *
 * https://leetcode.com/problems/shuffle-the-array/description/
 *
 * algorithms
 * Easy (88.39%)
 * Likes:    5590
 * Dislikes: 282
 * Total Accepted:    638.7K
 * Total Submissions: 722.6K
 * Testcase Example:  '[2,5,1,3,4,7]\n3'
 *
 * Given the array nums consisting of 2n elements in the form
 * [x1,x2,...,xn,y1,y2,...,yn].
 *
 * Return the array in the form [x1,y1,x2,y2,...,xn,yn].
 *
 *
 * Example 1:
 *
 *
 * Input: nums = [2,5,1,3,4,7], n = 3
 * Output: [2,3,5,4,1,7]
 * Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is
 * [2,3,5,4,1,7].
 *
 *
 * Example 2:
 *
 *
 * Input: nums = [1,2,3,4,4,3,2,1], n = 4
 * Output: [1,4,2,3,3,2,4,1]
 *
 *
 * Example 3:
 *
 *
 * Input: nums = [1,1,2,2], n = 2
 * Output: [1,2,1,2]
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= n <= 500
 * nums.length == 2n
 * 1 <= nums[i] <= 10^3
 *
 */

// @lc code=start

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int *shuffle(int *nums, int numsSize, int n, int *returnSize)
{
    int i, j = 0, k = 0;
    int a[n], b[n];
    int *arr = (int *)malloc(numsSize * sizeof(int));
    for (i = 0; i < n; i++)
    {
        a[i] = nums[i];
    }
    for (i = 0; i < n; i++)
    {
        b[i] = nums[n + i];
    }
    for (i = 0; i < numsSize; i++)
    {
        if (i % 2 == 0)
        {
            arr[i] = a[j];
            j++;
        }
        else if (i % 2 != 0)
        {
            arr[i] = b[k];
            k++;
        }
    }
    *returnSize = numsSize;
    return arr;
}
// @lc code=end
