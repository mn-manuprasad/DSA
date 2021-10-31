# https://leetcode.com/problems/sqrtx/

'''
let x be the number
Squre root of x should be less than or equal to the half of x so all we need to do is to check for the answer between 1 and half of x
'''

class Solution:
    def mySqrt(self, x: int) -> int:
        start = 1
        end = x
        while(start<=end):
            mid = start + (end-start)//2
            if mid*mid>x:
                end  = mid-1
            elif mid*mid<x:
                start = mid
            else:
                return mid
        return end
        
print(Solution().mySqrt(int(input())))