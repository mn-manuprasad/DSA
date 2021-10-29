# https://leetcode.com/problems/split-array-largest-sum/
# https://www.youtube.com/watch?v=OmJuyKaGGjs (Solution)
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


Logic : 

We need to minimize the largest sum among the sub arrays

The maximum pieces we can do of an array is equal to the size of the array
       And, the minimum would be just one
       
       If m = length of array, our final answer would be the largest element in the array(ie, The maximum number of partitions that we can make)
       If m = 1, our final answer is the sum of the array(ie, The minimum number of partition that we can make is 1)
       
       After, getting the range, we can think of applying binary search - to find the most optimal solution
'''




class Solution():
    def splitArray(self,nums,m):
        def isPossible(s):
            split = 0
            cur_sum = 0
            for num in nums:
                cur_sum+=num
                if cur_sum > s:
                    split+=1
                    cur_sum = num
                    if split > m-1:
                        return False
            return True

        start = max(nums)
        end = sum(nums)
        while(start<end):
            mid = start+(end-start)//2
            if(isPossible(mid)):
                end = mid
            else:
                start = mid+1
        return start


    





ls = [1,2,4,6]
m = 3
ans = Solution().splitArray(ls, m)
print(ans)