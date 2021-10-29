# https://leetcode.com/problems/find-smallest-letter-greater-than-target/

'''
Given a characters array letters that is sorted in non-decreasing order and a character target, return the smallest character in the array that is larger than target.

Note that the letters wrap around.

For example, if target == 'z' and letters == ['a', 'b'], the answer is 'a'.

'''

class Solution():
    def nextGreatestLetter(self,ls,target):
        start = 0
        end  = len(ls)-1
        while start <= end:
            mid = (start+end) // 2
            if target >= ls[mid]:
                # end = mid-1
                start = mid+1
            else:
                # start = mid+1
                end = mid-1
                
        return ls[start%len(ls)]




ls = ["c","f","j"]
target = 'c'
ans = Solution().nextGreatestLetter(ls, target)
print(ans)

