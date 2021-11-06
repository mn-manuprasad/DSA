# https://leetcode.com/problems/fair-candy-swap/

'''
        Explanation
        
        Sa = sumOfAliceCandies
        Sb = sumOfBobCandies
        
        Alice gives  -> x candies   =>    Bob Receives   -> x candies
        Bob gives    -> y candies   =>    Alice Recevies -> y candies
        
        After the operation Sum of candies of both should be equal
        
        Sa-x+y = Sb-y+x 
        [
            Sa+2y = Sb+2x
            2y = Sb - Sa + 2x
            y = (Sb - Sa + 2x)/2
        ]   
        
        So for every x we need to seach for a y in bob's array which 
        satisfies y = (Sb - Sa + 2x)/2 
        
        For Searching We can either use Binary Search which has O(log n) complexity 
        or set in python which has O(1) as the time complexity
                   
        
'''
class Solution:
    def fairCandySwap(self, aliceSizes, bobSizes):
        Sa = sum(aliceSizes)
        Sb = sum(bobSizes)
        
        setB = set(bobSizes)
        
        for x in aliceSizes:
            if (Sb-Sa + 2*x)//2 in setB:
                return [x,(Sb-Sa + 2*x)//2]


aliceSizes = [1,2,5]
bobSizes = [2,4]

print(Solution().fairCandySwap(aliceSizes, bobSizes))

        