#https://leetcode.com/problems/peak-index-in-a-mountain-array/


class Solution():
    def peakElement(self,ls):
        start = 0
        end = len(ls)-1
        while(start<end):
            mid = start + (end-start)//2
            if ls[mid] > ls[mid+1]:
                end = mid
            elif ls[mid] < ls[mid+1]:
                start = mid +1
        return start


ls = [0,2,1,0]
ans = Solution().peakElement(ls)
print(ls[ans])