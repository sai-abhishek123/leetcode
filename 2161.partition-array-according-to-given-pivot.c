/*
 * @lc app=leetcode id=2161 lang=c
 *
 * [2161] Partition Array According to Given Pivot
 *
 * https://leetcode.com/problems/partition-array-according-to-given-pivot/description/
 *
 * algorithms
 * Medium (84.68%)
 * Likes:    1037
 * Dislikes: 81
 * Total Accepted:    66.9K
 * Total Submissions: 79.1K
 * Testcase Example:  '[9,12,5,10,14,3,10]\n10'
 *
 * You are given a 0-indexed integer array nums and an integer pivot. Rearrange
 * nums such that the following conditions are satisfied:
 *
 *
 * Every element less than pivot appears before every element greater than
 * pivot.
 * Every element equal to pivot appears in between the elements less than and
 * greater than pivot.
 * The relative order of the elements less than pivot and the elements greater
 * than pivot is maintained.
 *
 * More formally, consider every pi, pj where pi is the new position of the
 * i^th element and pj is the new position of the j^th element. For elements
 * less than pivot, if i < j and nums[i] < pivot and nums[j] < pivot, then pi <
 * pj. Similarly for elements greater than pivot, if i < j and nums[i] > pivot
 * and nums[j] > pivot, then pi < pj.
 *
 *
 *
 *
 * Return nums after the rearrangement.
 *
 *
 * Example 1:
 *
 *
 * Input: nums = [9,12,5,10,14,3,10], pivot = 10
 * Output: [9,5,3,10,10,12,14]
 * Explanation:
 * The elements 9, 5, and 3 are less than the pivot so they are on the left
 * side of the array.
 * The elements 12 and 14 are greater than the pivot so they are on the right
 * side of the array.
 * The relative ordering of the elements less than and greater than pivot is
 * also maintained. [9, 5, 3] and [12, 14] are the respective orderings.
 *
 *
 * Example 2:
 *
 *
 * Input: nums = [-3,4,3,2], pivot = 2
 * Output: [-3,2,4,3]
 * Explanation:
 * The element -3 is less than the pivot so it is on the left side of the
 * array.
 * The elements 4 and 3 are greater than the pivot so they are on the right
 * side of the array.
 * The relative ordering of the elements less than and greater than pivot is
 * also maintained. [-3] and [4, 3] are the respective orderings.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= nums.length <= 10^5
 * -10^6 <= nums[i] <= 10^6
 * pivot equals to an element of nums.
 *
 *
 */

// @lc code=start
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int *pivotArray(int *nums, int numsSize, int pivot, int *returnSize)
{
    int c1 = 0, c2 = 0, c3 = 0, i, j = 0, k = 0, o = 0;
    for (i = 0; i < numsSize; i++)
    {
        if (nums[i] < pivot)
            c1++;
        else if (nums[i] > pivot)
            c2++;
        else if (nums[i] == pivot)
            c3++;
    }
    int *l = (int *)malloc(c1 * sizeof(int));
    int *r = (int *)malloc(c2 * sizeof(int));
    int *c = (int *)malloc(c3 * sizeof(int));
    for (i = 0; i < numsSize; i++)
    {
        if (nums[i] < pivot)
        {
            l[j] = nums[i];
            j++;
        }
        else if (nums[i] > pivot)
        {
            r[k] = nums[i];
            k++;
        }
        else if (nums[i] == pivot)
        {
            c[o] = nums[i];
            o++;
        }
    }
    j = 0, k = 0;
    int *arr = (int *)malloc((numsSize) * sizeof(int));
    for (i = 0; i < c1; i++)
    {
        arr[i] = l[i];
    }
    for (i = c1; i < c1 + c3; i++)
    {
        arr[i] = c[j];
        j++;
    }
    for (i = c1 + c3; i < numsSize; i++)
    {
        arr[i] = r[k];
        k++;
    }
    *returnSize = numsSize;
    return arr;
}
// @lc code=end
