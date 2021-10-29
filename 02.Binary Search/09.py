#https://leetcode.com/problems/find-in-mountain-array/

class Solution():
    def findInMountainArray(self,ls,target):
        peak = self.findPeakIndex(ls, target)

        firstTry = self.binary(ls, 0, peak, target)
        if not(firstTry==-1):
            return firstTry
        else:
            return self.binary(ls, peak+1, len(ls)-1, target)
    
    def findPeakIndex(self,ls,target):
        start = 0
        end = len(ls)-1
        while(start < end):
            mid = start + (end-start)//2
            if ls[mid] > ls[mid+1]:
                end = mid
            elif ls[mid] < ls[mid+1]:
                start = mid+1
        return start

    def binary(self,ls,start,end,target):
        ascending = True
        if ls[start] >= ls[end]:
            ascending = False
        if ascending:
            while start <= end :
                mid = (start+end)//2
                if target < ls[mid]:
                    end = mid-1
                elif target > ls[mid]:
                    start = mid+1
                else:
                    return mid
        else:
            while start <= end :
                mid = (start+end)//2
                if target < ls[mid]:
                    start = mid+1
                elif target > ls[mid]:
                    end = mid-1
                else:
                    return mid

        return -1





ls =  [1,2,5,6,4,3,1]
target = 3
ans = Solution().findInMountainArray(ls, target)
 
print(ans)