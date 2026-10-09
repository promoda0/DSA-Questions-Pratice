'''
1. Problem Statement

Given an array of integers representing daily data-processing volumes, determine the largest value recorded.

You must solve the problem without using Python's built-in `max()` function.

Return the largest integer present in the array. The array may contain positive integers, negative integers, or zero. Duplicate values are allowed, and the input is not necessarily sorted.
2. Constraints
Condition	Requirement
Array length	\(1 \leq n \leq 10^5\)
Element values	\(-10^9 \leq nums[i] \leq 10^9\)
Input type	List of integers
Empty array	Not allowed
Duplicate values	Allowed
Array order	Unsorted
Built-in max()	Not allowed
Sorting	Not required; aim for a single traversal
Expected result	One integer
Interview note: Negative values allowed hain, isliye hum assume nahi kar sakte ki largest value hamesha positive hogi.
3. Examples
Example 1 — Normal case
Input
nums = [12, 45, 7, 89, 23]
Output
89
Explanation
The largest value in the array is 89.

Example 2 — All negative values
Input
nums = [-15, -3, -27, -8]
Output
-3
Explanation
Among negative numbers, -3 is the largest because it is closest to zero.

Example 3 — Duplicate maximum
Input
nums = [6, 18, 18, 4, 10]
Output
18
Explanation
The largest value is 18, even though it occurs more than once.

Example 4 — Single element
Input
nums = [-42]
Output
-42
Explanation
Since the array contains only one element, that element is the largest.

Example 5 — Zero and negative values
Input
nums = [-9, 0, -2, -11]
Output
0
Explanation
Zero is greater than every negative value in the array.
4. Edge Cases to Test
Testing checklist

[ ] Single element
Input: {item.input} → Expected: {item.expected}


[ ] All negative numbers
Input: {item.input} → Expected: {item.expected}


[ ] All values equal
Input: {item.input} → Expected: {item.expected}


[ ] Zero is the largest
Input: {item.input} → Expected: {item.expected}


[ ] Repeated maximum
Input: {item.input} → Expected: {item.expected}


[ ] Boundary values
Input: {item.input} → Expected: {item.expected}

5. What the interviewer expects
- Correctly identify the largest value, including when all numbers are negative.
- Avoid the built-in max() function.
- Aim for \(O(n)\) time complexity by examining each element at most once.
- Use \(O(1)\) auxiliary space for an iterative solution.
- Explain why the initial value must be chosen carefully; assuming the largest value starts at 0 can produce an incorrect result for an all-negative array.
'''
