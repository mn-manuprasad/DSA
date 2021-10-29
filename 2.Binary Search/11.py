# Find the Rotation Count in Rotated Sorted array
# https://www.geeksforgeeks.org/find-rotation-count-rotated-sorted-array/

'''
Find the pivot position and the number of rations will be equal to pivot position + 1
'''

class Solution():
    
    def numberOfRotations(self,ls):
        ans = self.findPivot(ls)
        return ans+1

    def findPivot(self,ls):
        start = 0
        end = len(ls)-1
        while(start<=end):
            mid = start + (end-start)//2
            if ls[mid]>ls[mid+1]:
                return mid
            if ls[mid] < ls[mid-1]:
                return mid-1
            
            if ls[start] >= ls[mid]:
                end = mid-1
            else:
                start  = mid+1
        return -1  #if there is no pivot which means the array is not rotated


# ls = [2, 3, 6, 12]

ls = [4,5,6,7,0,1,2]

ans = Solution().numberOfRotations(ls)
print(ans)