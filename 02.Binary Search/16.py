# https://leetcode.com/problems/kth-missing-positive-number/
'''

BruteForce Approach

def findKthPositive(self, arr: List[int], k: int) -> int:
        count = 0
        for i in range(1,arr[len(arr)-1]+1):
            if i not in arr:
                count += 1
                if count==k:
                    return i
        return arr[len(arr)-1]+(k-count) '''


"""
    Optimal Solution Using Binary Search
    
    Since the numbers are continous and array is 0-indexed array so, at any index i the arr[i] should be i+1.
    If the value at index i is not i+1 then some number(s) must be missing.
    A simple logic to calculate the count of missing numbers till index i is,
    missingNumbers = arr[i] - (i+1)
    i.e,
    missingNumbers = current value at ith index - actual value at ith index.
    
    Now we just need to find when the missingNumbers count becomes greater than or equal to k.
    If missingNumbers count is less than k then kth missing number would definitely lie after mid. Else, it would lie before mid.
    
"""

def findKthPositive(arr, k):      
        start = 0
        end = len(arr) - 1
        
        while start <= end:
            mid = start + ((end - start) // 2)
            if arr[mid] - (mid+1) < k:
                start = mid + 1
            else:
                end = mid - 1
        return start + k
    
arr = [1,2,3,4]     
k = 2
print(findKthPositive(arr, k))     