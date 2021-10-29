# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

'''

'''
Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
'''

class Solution():
    def searchRange(self,ls,target):
        start = 0
        end = len(ls)-1
        ans = [-1,-1]  
        # First Checking For the first index
        start = self.findTarget(ls, target, findStartIndex=True)
        end = self.findTarget(ls, target, findStartIndex=False)
        ans[0]=start
        ans[1]=end
        return ans
    
    def findTarget(self,ls,target,findStartIndex ):
        start = 0
        end = len(ls)-1
        ans = -1
        while(start<=end):
            mid = (start+end)//2
            if target > ls[mid]:
                start = mid+1
            elif target < ls[mid]:
                end = mid-1
            else:
                ans = mid
                if findStartIndex:
                    end = mid-1
                else:
                    start = mid+1
        return ans
                




ls = [5,7,7,8,8,10]
target =  8
ans=Solution().searchRange(ls, target)
print(ans)


