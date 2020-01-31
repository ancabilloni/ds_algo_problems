""" https://leetcode.com/problems/4sum-ii/ 
O(n^2) solution
"""

from collections import defaultdict

class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        n = len(A)
        count = 0
        SumAB= defaultdict(lambda: 0)
        SumCD = defaultdict(lambda: 0)
        
        for i in range(n):
            for j in range(n):
                SumAB[A[i] + B[j]] += 1
                SumCD[C[i] + D[j]] += 1
                
        for key1 in SumAB:
            if -key1 in SumCD:
                count += SumAB[key1] * SumCD[-key1]
                            
        return count
