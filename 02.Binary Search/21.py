# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

class Solution:
    def search(self, nums, target):
        if not nums or len(nums) == 0: return False
        
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target: return True
            elif nums[mid] > nums[low]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            elif nums[mid] < nums[low]:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                low += 1 # duplicates so ignoare all same ones
        return False

nums = [2,5,6,0,0,1,2]
target = 0
print(Solution().search(nums, target))