# Ceiling Of a number

'''
  Celing of a number means that from the array find the smallest element in the array that is greater than or equal to the target number

  arr = [2,3,5,9,16,18]
  target = 15
  Here the answer will be = 16
   
  Because the number just greater the or equal to the target  is 16

  If there is no ceiling exists return no celing exists

 arr = [2,3,5,9,16,18]
 target  =  19

 answer : No Celing Exists

'''



'''
Concept

In Binary search if the target position is not found then the start index  will contain the value that is just greater than target

'''

class Solution():
    def ceiling(self,ls,target):
        start = 0
        end = len(ls)-1
        # if target  > ls[end]:
        #     return -1
        while start <= end :
            mid = (start+end)//2
            # or mid = start + (end-start) // 2
            if target > ls[mid]:
                start = mid+1
            elif target < ls[mid]:
                end = mid-1
            else:
                return mid
        return start




ls = [1,6,7,8,9,10,11,12,24,56]
target = 57
ans = Solution().ceiling(ls, target)
if ans==-1:
    print("No Celing Exists")
else:
    print(f"Answer is {ls[ans]}")