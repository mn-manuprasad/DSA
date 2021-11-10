# https://leetcode.com/problems/single-element-in-a-sorted-array/

class Solution:
    def singleNonDuplicate(self, nums):
        
        '''
        index-> 0 1 2 3 4  5  6  7  8 
        nums = [3,3,7,7,10,11,11,13,13]
        
        Findings  :
        
            1. Before the unique element Every element starts at even position and ends at an odd                          position 
            
            2. But after The unique elements every element starts at odd index and ends at odd even index
            
            3. Unique element will be at an even position
            
            So Two Possible values of mid can be an odd number or even number
            
            *if the mid is an odd number also mid==mid-1 then it means all the elements are in correct               order till the mid position so we need to check only from mid+1 (start=mid+1) *else we can               say end=mid-1 (beacuse the unique element will not be at odd index) 
            
            *if the mid value is an even number then we need to check mid==mid+1 if it is then we need to              change the start = mid+1 (because every element before unique element start at even index                and odd index) *else we need to change the end=mid beacuse end can be our potential answer
        
        '''
        start = 0
        end = len(nums)-1
        if end==0:
            return nums[0]
        
        
        while start<end:
            mid = start+(end-start)//2
            if mid%2!=0:
                if mid>0 and nums[mid]==nums[mid-1]:
                    start = mid+1
                else:
                    end = mid-1
            else:
                
                if mid<len(nums)-2 and nums[mid]==nums[mid+1]:
                    start=mid+1
                else:
                    end=mid
        return nums[start]
    
    


nums = [1,1,2,3,3,4,4,8,8]
print(Solution().singleNonDuplicate(nums))
    