# https://leetcode.com/problems/arranging-coins/

class Solution:
    def arrangeCoins(self, n: int) -> int:
        start = 1
        end = n
        while start<=end:
            mid = start+(end-start)//2
            s = (mid*(mid+1))//2
            if s > n:
                end = mid-1
            elif s/2 < n:
                start  = mid+1
            else:
                return mid
        return end


print(Solution().arrangeCoins(int(input())))