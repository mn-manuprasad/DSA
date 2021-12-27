class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        d = {}
        
        for i in range(len(numbers)):
            m = target - numbers[i]
            if m in d:
                return [d[m]+1,i+1]
            else:
                d[numbers[i]] = i
