class Solution:
    def findMin(self, nums):
        
        def findPivot():
            start = 0
            end = len(nums)-1
            while start<=end:
                mid = start+(end-start)//2
                
                if mid<end and nums[mid]>nums[mid+1]:
                    return mid
                if mid>start and nums[mid]<nums[mid-1]:
                    return mid-1
                
                if nums[start]>nums[mid]:
                    end = mid-1
                elif nums[start]<nums[mid]:
                    start = mid+1
                    
        
        
        start = 0
        end = len(nums)-1
        if nums[0]<nums[len(nums)-1]:
            return nums[0]
        elif end==0:
            return nums[end]
        else:
            pivot = findPivot()
            return nums[pivot+1]
            

nums =[3,4,5,1,2]
print(Solution().findMin(nums))
        