# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

# Given an array nums of integers, return how many of them contain an even number of digits.

'''
Input: nums = [12,345,2,6,7896]
Output: 2
Explanation: 
12 contains 2 digits (even number of digits). 
345 contains 3 digits (odd number of digits). 
2 contains 1 digit (odd number of digits). 
6 contains 1 digit (odd number of digits). 
7896 contains 4 digits (even number of digits). 
Therefore only 12 and 7896 contain an even number of digits.
'''

class solution():
    def findNumber(self,nums)->int :
        count = 0
        for i in nums:
            if i<0:
                i*=-1
            if len(str(i))%2==0:
                count+=1
        else:
            return count




nums = [-12,0,345,2,6,7896]
out = solution().findNumber(nums)
print(out)
