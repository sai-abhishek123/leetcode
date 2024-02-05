/*
 * @lc app=leetcode id=217 lang=c
 *
 * [217] Contains Duplicate
 *
 * https://leetcode.com/problems/contains-duplicate/description/
 *
 * algorithms
 * Easy (61.33%)
 * Likes:    11487
 * Dislikes: 1271
 * Total Accepted:    3.6M
 * Total Submissions: 5.9M
 * Testcase Example:  '[1,2,3,1]'
 *
 * Given an integer array nums, return true if any value appears at least twice
 * in the array, and return false if every element is distinct.
 *
 *
 * Example 1:
 * Input: nums = [1,2,3,1]
 * Output: true
 * Example 2:
 * Input: nums = [1,2,3,4]
 * Output: false
 * Example 3:
 * Input: nums = [1,1,1,3,3,4,3,2,4,2]
 * Output: true
 *
 *
 * Constraints:
 *
 *
 * 1 <= nums.length <= 10^5
 * -10^9 <= nums[i] <= 10^9
 *
 *
 */

// @lc code=start
typedef struct
{
    int key;
    UT_hash_handle hh;
} HashTableEntry;
bool containsDuplicate(int *nums, int numsSize)
{
    HashTableEntry *users = NULL, *tmp;
    for (int i = 0; i < numsSize; i++)
    {
        int val = nums[i];
        HASH_FIND_INT(users, &val, tmp);
        if (tmp)
        {
            HashTableEntry *current_entry, *tmp_entry;
            HASH_ITER(hh, users, current_entry, tmp_entry)
            {
                HASH_DEL(users, current_entry);
                free(current_entry);
            }
            return true;
        }
        tmp = (HashTableEntry *)malloc(sizeof(HashTableEntry));
        tmp->key = val;
        HASH_ADD_INT(users, key, tmp);
    }
    HashTableEntry *current_entry, *tmp_entry;
    HASH_ITER(hh, users, current_entry, tmp_entry)
    {
        HASH_DEL(users, current_entry);
        free(current_entry);
    }
    return false;
}
// @lc code=end
