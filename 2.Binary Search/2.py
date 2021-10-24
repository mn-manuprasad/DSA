# Order agnostic binary search
# Which means we don't know the array is sorted ascending or descending order


class Solution():
    def binary(self,ls,start,end,target):
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



# ls = [1,6,7,8,9,10,11,12,24,56]
ls = [56,24,12,11,10,9,8,7,6,1]
target=1
start=0
end=len(ls)-1

pos = Solution().binary(ls, start, end, target)

if not(pos)==-1:
    print(f'{target} found at index {pos}')
else:
    print(f'{target} not found')
