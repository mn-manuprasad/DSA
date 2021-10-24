# https://leetcode.com/problems/split-array-largest-sum/

'''
Given an array nums which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays.
 
Write an algorithm to minimize the largest sum among these m subarrays.

Input: nums = [7,2,5,10,8], m = 2
Output: 18

we can split nums into m subarrays in 4 ways

                        Largest sum

[7,2,5,10]  and [8]        24

[7,2,5] and [10,8]         18

[7,2] and [5,10,8]         23

[7]  and [2,5,10,8]        25

Here 18 is the smallest sum among the largest sum so the answer is 18

'''