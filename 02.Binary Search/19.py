# https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/

class Solution:
    def specialArray(self, nums):
        
        def binarySearch(target):
            start = 0
            ans = -1
            end = len(nums)-1
            while(start<=end):
                mid = start+(end-start)//2
                if nums[mid] > target:
                    end = mid-1
                elif nums[mid] < target:
                    start = mid+1
                else:
                    ans = mid
                    end = mid-1
            if ans==-1:
                return start
            else:
                return ans
                    
        nums.sort()
        l = len(nums)
        for i in range(0,nums[l-1]):
            pos = binarySearch(i)
            if l-pos == i:
                return i
        return -1

nums = [3,5]
print(Solution().specialArray(nums))