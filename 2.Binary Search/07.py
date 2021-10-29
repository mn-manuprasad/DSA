'''Find position of an element in a sorted array of infinite numbers

Suppose you have a sorted array of infinite numbers, how would you search an element in the array?

Since array is sorted, the first thing clicks into mind is binary search, but the problem here is that we don’t know size of array. 
If the array is infinite, that means we don’t have proper bounds to apply binary search. So in order to find position of key, first we find bounds and then apply binary search algorithm.
Let low be pointing to 1st element and high pointing to 2nd element of array, Now compare key with high index element, 
->if it is greater than high index element then copy high index in low index and double the high index. 
->if it is smaller, then apply binary search on high and low indices found. '''


class Solution():
    def findTarget(self,ls):
        size = 2
        start = 0
        end = 1
        while True:
            if target<=ls[end]:
                while(start<=end):
                    mid = start +  (end-start)//2
                    if target > ls[mid]:
                        start = mid +1
                    elif target < ls[mid]:
                        end = mid-1
                    else:
                        return mid
                return -1
            else:
                start = end + 1 
                size = size * 2
                end = start + size-1
                
                



ls=[1,2,3,4,5,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
target =  int(input())
pos =  Solution().findTarget(ls)
print(pos)


