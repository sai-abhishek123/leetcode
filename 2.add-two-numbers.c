/*
 * @lc app=leetcode id=2 lang=c
 *
 * [2] Add Two Numbers
 *
 * https://leetcode.com/problems/add-two-numbers/description/
 *
 * algorithms
 * Medium (42.14%)
 * Likes:    29847
 * Dislikes: 5845
 * Total Accepted:    4.3M
 * Total Submissions: 10.1M
 * Testcase Example:  '[2,4,3]\n[5,6,4]'
 *
 * You are given two non-empty linked lists representing two non-negative
 * integers. The digits are stored in reverse order, and each of their nodes
 * contains a single digit. Add the two numbers and return the sum as a linked
 * list.
 *
 * You may assume the two numbers do not contain any leading zero, except the
 * number 0 itself.
 *
 *
 * Example 1:
 *
 *
 * Input: l1 = [2,4,3], l2 = [5,6,4]
 * Output: [7,0,8]
 * Explanation: 342 + 465 = 807.
 *
 *
 * Example 2:
 *
 *
 * Input: l1 = [0], l2 = [0]
 * Output: [0]
 *
 *
 * Example 3:
 *
 *
 * Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
 * Output: [8,9,9,9,0,0,0,1]
 *
 *
 *
 * Constraints:
 *
 *
 * The number of nodes in each linked list is in the range [1, 100].
 * 0 <= Node.val <= 9
 * It is guaranteed that the list represents a number that does not have
 * leading zeros.
 *
 *
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode *addTwoNumbers(struct ListNode *l1, struct ListNode *l2)
{

    {
        // Initialize a dummy node to hold the result
        struct ListNode *dummy = malloc(sizeof(struct ListNode));
        dummy->val = 0;
        dummy->next = NULL;
        struct ListNode *current = dummy;
        int carry = 0;

        // Iterate over both linked lists until we reach the end
        while (l1 || l2)
        {
            // Extract the values of the current nodes, or use 0 if the linked list is shorter
            int x = l1 ? l1->val : 0;
            int y = l2 ? l2->val : 0;

            // Perform the addition and update the carry
            int s = x + y + carry;
            carry = s / 10;
            current->next = malloc(sizeof(struct ListNode));
            current->next->val = s % 10;
            current->next->next = NULL;

            // Advance to the next nodes
            current = current->next;
            l1 = l1 ? l1->next : NULL;
            l2 = l2 ? l2->next : NULL;
        }

        // If there is a carry left, add a new node to the result
        if (carry > 0)
        {
            current->next = malloc(sizeof(struct ListNode));
            current->next->val = carry;
            current->next->next = NULL;
        }

        // Return the result, skipping the dummy node
        return dummy->next;
    }
}
// @lc code=end
