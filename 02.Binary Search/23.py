# https://leetcode.com/problems/find-right-interval/
# https://www.youtube.com/watch?v=VEBbumHmps8

class Solution:
    def findRightInterval(self, intervals):
        sorted = []
        n = len(intervals)
        
        for i in range(n):
            sorted.append([intervals[i],i])
        
        sorted.sort()
        result = [0]*n
        
        if n==1:
            return [-1]
        else:
            for i in range(n):
                start = i
                end = len(sorted)-1
                target = sorted[i][0][1]
                while(start<=end):
                    mid = start + (end-start)//2
                    if target > sorted[mid][0][0]:
                        start = mid+1
                    elif target < sorted[mid][0][0]:
                        end = mid-1
                    else:
                        result[sorted[i][1]] = sorted[mid][1]
                        break
                else:
                    if start==n:
                        result[sorted[i][1]] = -1
                    else:
                        result[sorted[i][1]] = sorted[start][1]
        return result
                
                

intervals = [[3,4],[2,3],[1,2]]    

print(Solution().findRightInterval(intervals))
        
        