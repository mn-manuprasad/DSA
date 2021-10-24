# https://leetcode.com/problems/search-in-rotated-sorted-array/

'''
arr = [4,5,6,7,0,1,2]

Here 7 is the pivot element. Once we find the pivot element we can use binary search to solve this
      note => Pivot is the largest number in the rotated array
   Find Pivot ?
        1. When  arr[mid] > arr[mid+1] (7>0), arr[mid] is the pivot element
        beacuse the elements before and after the pivot element is sorted in ascending order and the values after the pivot element should be less than the pivot element so when an element is greater than its very next element thats is our pivot element ( Violating the the ascending rule their [7,0]=> Descending order)

        2. When the arr[mid] (0) < arr[mid-1] (7) This also founds the pivot element

        3. 
                arr = [4,5,6,7,0,1,2]
                       s         m e

               if arr[satrt] >= arr[mid] :
                    end = mid-1
                   we only need to search from satrt to mid-1 to find the pivot
                   beacuse the element after mid(including mid) is less than the pivot(beacause it is less than start)
                
                 arr = [4,5,6,7,0,1,2]
                        s   m       e

                if arr[start] < arr [mid]:
                    start = mid + 1

                    beacuse from points 1 and 2 we know that its not the pivot element

'''


class Solution():
    def findTarget(self,ls,target):
        pivot  = self.findPivot(ls)
        #if we dont find  pivot which means the array is not rotated
        if(pivot==-1):
            # Do Normal Binary Serach
            return self.binary(ls, 0, len(ls)-1, target)
        else:
            ans = self.binary(ls, 0, pivot, target)
            if not(ans==-1):
                return ans
            else:
                return self.binary(ls,pivot+1,len(ls)-1,target)

    def findPivot(self,ls):
        start = 0
        end = len(ls)-1
        while(start<=end):
            mid = start + (end-start)//2
            if mid<end and ls[mid] > ls[mid+1]:
                return mid
            if mid > start and ls[mid] < ls[mid-1]:
                return mid-1
            if ls[start] > ls[mid]:
                end = mid-1
            else: 
                start = mid + 1
        return -1
         
    def binary(self,ls,start,end,target):
        while start <= end :
            mid = (start+end)//2
            if target < ls[mid]:
                end = mid-1
            elif target > ls[mid]:
                start = mid+1
            else:
                return mid
        return -1





ls =  [ 4,5,6,7,0,1,2,3]
# ls = [3,2,2,2,3]
ans  = Solution().findTarget(ls, target)
print(ans)