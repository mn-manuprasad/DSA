#  Binary Search Implementation

class Solution():
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



ls = [1,6,7,8,9,10,11,12,24,56]
target=57
start=0
end=len(ls)-1

pos = Solution().binary(ls, start, end, target)

if not(pos)==-1:
    print(f'{target} found at index {pos}')
else:
    print(f'{target} not found')

