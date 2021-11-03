# https://leetcode.com/problems/intersection-of-two-arrays/
class Solution:
    def intersection(self,nums1,nums2):      
        def binarySearch(target):
            start = 0
            end = len(nums2)-1
            while(start<=end):
                mid = start+(end-start)//2
                if target > nums2[mid]:
                    start = mid+1
                elif target < nums2[mid]:
                    end = mid-1
                else:
                    return True
            return False

        nums2.sort()
        result = set()
        for i in nums1:
            if binarySearch(i):
                result.add(i)
        return list(result)


nums1 =  [4,9,5]
nums2 = [9,4,9,8,4]
print(Solution().intersection(nums1, nums2))
                
                
        