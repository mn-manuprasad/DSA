# Flooor Of a Number

'''
  Floor of a number means that from the array find the greatest element in the array that is smaller than or equal to the target number

  arr = [2,3,5,9,16,18]
  target = 15
  Here the answer will be = 9
   
  Because the number just smaller than or equal to the target  is 9

  If there is no floor exists return no flooor exists

 arr = [2,3,5,9,16,18]
 target  =  1

 answer : No Floor Exists

'''



'''
Concept

In Binary search, if the target position is not found then the end index  will contain the value that is just smaller than  the target

'''

class Solution():
    def floor(self,ls,target):
        start = 0
        end = len(ls)-1
        if target < ls[0]:
            return -1

        while start <= end :
            mid = (start+end)//2
            # or mid = start + (end-start) // 2
            if target > ls[mid]:
                start = mid+1
            elif target < ls[mid]:
                end = mid-1
            else:
                return mid
        return end




ls = [1,6,7,8,9,10,11,12,24,56]

target = 0
ans = Solution().floor(ls, target)
if ans==-1:
    print("No Floor Exists")
else:
    print(f"Answer is {ls[ans]}")